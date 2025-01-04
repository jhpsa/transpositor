from scipy.io import wavfile
from matplotlib import pyplot as plt
import numpy as np
import soundfile as sf


root_path = './audios/flute_a4.wav' #faixa de áudio da nota A4 em uma flauta

root_path2 = './audios/new_flute.wav' #arquivo de áudio que receberá o áudio transposto

fs, data = wavfile.read(root_path) #lendo a faixa de áudio da flauta e atribuindo os valores do frequency rate e do vetor data

data = np.array(data, dtype=float) #transformando o vetor em um array para trabalhar melhor com as funções do numpy

data = (data - np.mean(data)) / np.std(data) #normalizando os valores do vetor data

time = np.arange(0, len(data) * 1/fs, 1/fs) #criando a coordenada x de tempo
plt.axis([1,1.005,-3,2]) #dando zoom no gráfico para poder observar o formato das ondas senoidais
plt.ylabel("Amplitude normalizada")
plt.xlabel("Tempo (s)")
plt.plot(time, data) #criando o gráfico

plt.savefig('./images/grafico1_tempo.png') #salvando o gráfico em uma imagem
plt.close()

fftdata = np.fft.fft(data) #aplicando a transformada rápida de fourier no vetor data

#criando um vetor com o módulo da parte real das frequências
fftdatafreq = np.zeros((len(data)))
for i in range(len(fftdata)):
    fftdatafreq[i] = abs(fftdata[i].real)

#criando um gráfico que vai até metade da quantidade das frequências, já que a transformada de Fourier é uma
#função simétrica no ponto médio do dóminio da função

#plt.axis([0,10000,0,16000])
plt.ylabel("Amplitude")                 
plt.xlabel("Frequência (Hz)")
plt.plot(time[:len(fftdatafreq) // 2], fftdatafreq[:len(fftdatafreq) // 2])

plt.savefig('./images/grafico1_frequencia.png') #salvando o gráfico em uma imagem
plt.close()

maxfreq = np.argmax(fftdatafreq) #procurando o maior valor no vetor fftdatafreq
print('A frequência de maior amplitude formou', maxfreq, 'ondas senoidais.')

t = len(data) / fs #calculando o tempo de duração do áudio
print('A duração da faixa de áudio é de', t, 'segundos.')

domfreq = maxfreq / t #descobrindo o valor da frequência dominante
print('A frequência dominante é de', domfreq, 'Hz.')

n = 19 #número de semitons a aumentar (ou diminuir, se n < 0) ao tom da nota
new_fs = fs * (2**(n/12)) #calculando o novo frequency sample

#criando um vetor com as novas frequências desejadas
new_fftdatafreq = np.zeros((len(data)))
for i in range(len(fftdata)):
    new_fftdatafreq[i] = (abs(fftdata[i].real) * (new_fs/fs))

#criando o novo gráfico
#plt.axis([0,10000,0,16000])
plt.ylabel("Amplitude")
plt.xlabel("Frequência (Hz)")
plt.plot(time[:len(new_fftdatafreq) // 2], new_fftdatafreq[:len(new_fftdatafreq) // 2])

plt.savefig('./images/grafico2_frequencia.png') #salvando o gráfico em uma imagem
plt.close()

new_maxfreq = np.argmax(new_fftdatafreq) #procurando o maior valor no vetor new_fftdatafreq
print('A frequência de maior amplitude continua formando', new_maxfreq, 'ondas senoidais.')

new_t = len(data) / new_fs #calculando o tempo de duração do novo áudio
print('A duração da nova faixa de áudio é de', new_t, 'segundos.')

new_domfreq = new_maxfreq / new_t #descobrindo o valor da nova frequência dominante
print('O valor da nova frequência dominante é de', new_domfreq, 'Hz.')

new_data = np.fft.ifft(fftdata).real #aplicando a transformada de Fourier inversa com a parte real dos valores do vetor fftdata

sf.write(root_path2, new_data, int(new_fs)) #escrevendo a nova faixa de áudio no arquivo 'new_flute.wav'

new_data = np.array(new_data, dtype=float) #transformando o vetor new_data em um array do numpy

new_data = (new_data - np.mean(new_data)) / np.std(new_data) #normalizando

new_time = time = np.arange(0, len(new_data) * 1/new_fs, 1/new_fs) #criando a nova coordenada x de tempo
plt.axis([0.2,0.201,-3,2])
plt.ylabel("Amplitude normalizada")
plt.xlabel("Tempo (s)")
plt.plot(new_time, new_data) #criando o novo gráfico

plt.savefig('./images/grafico2_tempo.png') #salvando o gráfico em uma imagem
plt.close()