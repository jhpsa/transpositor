# Transpositor de faixas de áudio utilizando Transformada de Fourier (algoritmo FFT)
## Projeto realizado para a matéria de Álgebra Linear cursada na UFRJ no semestre 2019.2
- transpositor.py: lê a faixa de áudio de um arquivo .wav inicialmente no domínio do tempo, transforma para o domínio da frequência com a FFT, descobre sua frequência dominante (tom), acrescenta ou decrescenta n semitons, descobre a nova frequência dominante (confirmando o tom esperado), transforma de volta para o domínio do tempo com a FFT inversa e escreve em outro arquivo .wav
- audios: arquivos da faixa de áudio original (flute_a4.wav) e a transposta (new_flute.wav)
- images: gráficos de cada uma das etapas dos domínios do áudio sendo transposto (grafico1_tempo.png + FFT -> grafico1_frequencia.png, + n semitons -> grafico2_frequencia.png, + FFT inversa -> grafico2_tempo.png)
- Trabalho original com maiores explicações: https://colab.research.google.com/drive/1EvAzoYi6z9it1BOCzmeZycOYHSP35YaQ?usp=sharing
