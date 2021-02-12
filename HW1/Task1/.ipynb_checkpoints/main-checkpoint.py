{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 134,
   "metadata": {},
   "outputs": [],
   "source": [
    "import re\n",
    "import numpy\n",
    "import pandas as pd\n",
    "from scipy import spatial"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 135,
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "text = open(\"sentences.txt\", \"r\")\n",
    "sentences = []\n",
    "for line in text:\n",
    "    sentences.append(line.strip().lower())\n",
    "# print(len(sentences))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 136,
   "metadata": {},
   "outputs": [],
   "source": [
    "words = {}\n",
    "i = 0\n",
    "ind = 0\n",
    "sent_ww = sentences.copy()\n",
    "for line in sent_ww:\n",
    "    line = re.split('[^a-z]', line)\n",
    "    sent_ww[i] = line\n",
    "    i+=1\n",
    "    for w in line:\n",
    "        if w not in words and w!='':\n",
    "            words[w] = ind\n",
    "            ind+=1\n",
    "\n",
    "# print(len(words))\n",
    "# print(sentences)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 137,
   "metadata": {},
   "outputs": [],
   "source": [
    "num_w = len(words)\n",
    "num_s = len(sentences)\n",
    "\n",
    "matrix = numpy.zeros((num_s, num_w))\n",
    "\n",
    "for i in range(num_s):\n",
    "    sen_w = sent_ww[i]\n",
    "    for x in sen_w:\n",
    "        if x!='':\n",
    "            matrix[i][words[x]] += 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 138,
   "metadata": {},
   "outputs": [],
   "source": [
    "distances = {}\n",
    "\n",
    "first_sentence_metric = matrix[0, :]\n",
    "for i in range(num_s):\n",
    "    cmp_sentence_metric = matrix[i, :]\n",
    "    \n",
    "    distances[i] = spatial.distance.cosine(first_sentence_metric, cmp_sentence_metric)\n",
    "    \n",
    "# print(distances)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 139,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "distances_df = pd.DataFrame.from_dict(distances, orient = 'index')\n",
    "distances_df.columns = ['distance']\n",
    "distances_df['sentence'] = list(map(lambda x: sentences[x], distances_df.index.values))\n",
    "# print(sentences[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 140,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>distance</th>\n",
       "      <th>sentence</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0.000000</td>\n",
       "      <td>in comparison to dogs, cats have not undergone...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>0.732739</td>\n",
       "      <td>domestic cats are similar in size to the other...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0.777089</td>\n",
       "      <td>in one, people deliberately tamed cats in a pr...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>21</th>\n",
       "      <td>0.825036</td>\n",
       "      <td>the fifth major update to mac os x, leopard, c...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>0.832817</td>\n",
       "      <td>cat command is one of the basic commands that ...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>0.839643</td>\n",
       "      <td>when you type simply cat command without any a...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>0.840636</td>\n",
       "      <td>since apple moved to using intel processors in...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>20</th>\n",
       "      <td>0.842757</td>\n",
       "      <td>mac os x mountain lion installs in place, so y...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0.864474</td>\n",
       "      <td>a common interactive use of cat for a single f...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>0.870359</td>\n",
       "      <td>leopard was released on october 26, 2007 as th...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>0.874012</td>\n",
       "      <td>according to apple, leopard contains over 300 ...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>0.880477</td>\n",
       "      <td>using cat command, the lines received from std...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>0.884272</td>\n",
       "      <td>cat with one named file is safer where human e...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19</th>\n",
       "      <td>0.888544</td>\n",
       "      <td>the mountain lion release marks the second tim...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0.895172</td>\n",
       "      <td>cats can hear sounds too faint or too high in ...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>0.905509</td>\n",
       "      <td>in terms of legibility, a sequence of commands...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>0.925875</td>\n",
       "      <td>however, if the output is piped or redirected,...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>0.940239</td>\n",
       "      <td>the domesticated cat and its closest wild ance...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15</th>\n",
       "      <td>0.944272</td>\n",
       "      <td>as of mid 2010, some apple computers have firm...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>0.944272</td>\n",
       "      <td>apple has released a small patch for the three...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0.952754</td>\n",
       "      <td>as cat simply catenates streams of bytes, it c...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>0.956645</td>\n",
       "      <td>os x mountain lion was released on july 25, 20...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    distance                                           sentence\n",
       "0   0.000000  in comparison to dogs, cats have not undergone...\n",
       "6   0.732739  domestic cats are similar in size to the other...\n",
       "4   0.777089  in one, people deliberately tamed cats in a pr...\n",
       "21  0.825036  the fifth major update to mac os x, leopard, c...\n",
       "10  0.832817  cat command is one of the basic commands that ...\n",
       "12  0.839643  when you type simply cat command without any a...\n",
       "16  0.840636  since apple moved to using intel processors in...\n",
       "20  0.842757  mac os x mountain lion installs in place, so y...\n",
       "2   0.864474  a common interactive use of cat for a single f...\n",
       "13  0.870359  leopard was released on october 26, 2007 as th...\n",
       "14  0.874012  according to apple, leopard contains over 300 ...\n",
       "11  0.880477  using cat command, the lines received from std...\n",
       "8   0.884272  cat with one named file is safer where human e...\n",
       "19  0.888544  the mountain lion release marks the second tim...\n",
       "3   0.895172  cats can hear sounds too faint or too high in ...\n",
       "9   0.905509  in terms of legibility, a sequence of commands...\n",
       "7   0.925875  however, if the output is piped or redirected,...\n",
       "5   0.940239  the domesticated cat and its closest wild ance...\n",
       "15  0.944272  as of mid 2010, some apple computers have firm...\n",
       "18  0.944272  apple has released a small patch for the three...\n",
       "1   0.952754  as cat simply catenates streams of bytes, it c...\n",
       "17  0.956645  os x mountain lion was released on july 25, 20..."
      ]
     },
     "execution_count": 140,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "distances_df.sort_values('distance')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}