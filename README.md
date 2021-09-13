# desafioUAM
Trabalho realizado para a disciplina de técnica de redação UAM
Universidade Anhembi Morumbi

Projeto N1 – Parte 1

Observações Gerais

1. Trabalho pode ser feito de três a cinco pessoas. Caso opte por fazer individualmente, converse
com o professor por mensagem privada.
2. É necessário realizar a entrega até as 23:59 do dia 15/09
3. Compreender o enunciado e o problema proposto faz parte da avaliação


Situação Problema

Muitos jogos de RPG são baseados em explorar dungeons, ou seja, explorar cavernas,
calabouços, florestas e todo tipo de lugar desconhecido.
Hoje você será o líder de uma guilda de heróis!
Como todo bom líder, você deverá guiar os guerreiros através do labirinto.
As regras para a travessia do labirinto são bastante simples. Toda a guilda começará na
sala 1 e a partir dela pode-se escolher 2 opções diferentes:

• 1 – Caminho vermelho (ou direita);
• 2 – Caminho preto (ou esquerda);

Você precisará criar a lógica para fazer com que por meio de interações com o usuário
seja possível avançar pelos caminhos do labirinto. Considere que “o mapa” culto é
idêntico a este:

Note que o caminho preto da sala 8 leva à um local desconhecido, isso porque esta
dungeon é controlada por criaturas místicas que dominam o tempo-espaço e criaram
um portal! Toda vez que os personagens escolherem o caminho preto estando na sala
8 é preciso sortear o seu destino.
Podendo ser qualquer sala entre 1, 2, 3, 4 ou 5.
O seu programa deve fazer com que a guilda inicie na sala 1 e possa escolher entre o
caminho vermelho e preto na estrutura indicada anteriormente. Ele deverá funcionar
todo em console, não é preciso criar nenhum tipo de gráfico.
O programa deve iniciar cada interação notificando a sala que o jogador está e mostrando as
opções:

Algumas regras que precisam ser implementadas:

▪ Os heróis vencem ao chegar na Sala 9;

▪ A sala 6 tem realmente uma única possibilidade;

▪ Os heróis perdem se levarem 7 ou mais interações para chegarem na sala 9;

▪ Cada vez que os heróis escolhem um caminho é considerado 1 interação.

▪ Você precisa utilizar um laço de repetição, podendo ser o comando “while”;

▪ Dentro do laço de repetição você poderá incluir somente UM BLOCO de comando “if”
(com direito a um elif e um else, mas sem outros ifs internos) e NENHUM comando
“switch-case” (os demais comandos não possuem limitação);

▪ Fora do laço de repetição você poderá utilizar quantos comandos precisar.
