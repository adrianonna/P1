# Curriculum Vitae Estilizado

O Elon Musk gostaria de criar seu Curriculum Vitae, a princípio ele forneceu, textualmente, algumas informações que estão disponíveis no arquivo [site](site.zip). Nele encontram-se sua foto e algumas descrições, que juntos deverão ser apresentados em um navegador Web, conforme ilustra a *Figura 1*.

*Figura 1* - Layout do Currículum com Estilo
![Layout Curriculum](screen-curriculum.png)

Para alcançar tal propósito tente adicionar alguns estilos sugeridos a seguir por meio da linguagem CSS. **Obs.:** Os arquivos e diretórios do site apresentam a estrutura a seguir:

```
site
├── css
│   └── style.css
├── img
│   └── elon.jpg
├── index.html
└── pages
    └── resumo.html
```

As instruções passadas para gerar o currículos, conforme a *Figura 1*, são:

**INSTRUÇÃO 1.** Aplique ao &lt;h1> a tipo de fonte do google Audiowide, da família cursiva, e com o tamanho da fonte igual a 30px. Obs: A URL da fonte citada é:
https://fonts.googleapis.com/css?family=Audiowide.

**INSTRUÇÃO 2.** Adicione no &lt;h2> o border-radius com valor de 5px.

**INSTRUÇÃO 3.** Acrescente no final do hyperlink `leia mais` o ícone `launch` do Material Icon do Google. No entanto, no documento, altere o tamanho de sua fonte para 1em. Altere também a altura da linha do ícone e também dos paragráfos para 1.5em. Obs: A URL do ícone citado é: https://fonts.googleapis.com/icon?family=Material+Icons.

**INSTRUÇÃO 4.** Crie um botão conforme a Figura 2 composto pelo ícone fa-arrow-circle-left, do Fontawesome, e a palavra `voltar`. Este botão deverá estar em um hiperlink referenciando o arquivo `index.html`. Internamente o botão deverá conter uma classe chamada `btn`, que define o tamanho de fonte de 1.3em. Porém, quando o cursor estiver sobre este botão a cor do texto deverá ser branca, o plano de fundo darkblue e sem o sublinhado. Obs: A URL do ícone citado é: https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css.

*Figura 2* - Aparências do botão voltar <br>
![Aparências do botão voltar](button.png)


**INSTRUÇÃO 5.** Adicione ao bloco, cujo o id é `social`, três hiperlinks, cada um contendo os seguintes ícones do Fontawesome: fa-facebook-square, fa-twitter-square, fa-linkedin-square. Estes hiperlinks devem estar centralizados dentro do bloco, com a cor de texto branca e tamanho de fonte 2em. Os ícones fa-facebook-square, fa-twitter-square, fa-linkedin-square devem ser apresentados, respectivamente, nas cores navy, dodgerblue, navy.

**INSTRUÇÃO 6.** Na visualização de impressao de ambos os documentos html:

**a)** O &lt;body> e o &lt;h1> devem apresentar a cor de texto preta e o tipo de fonte `Times, serif`;

**b)** O Título &lt;h1> de id `elon` deve estar alinhado a esquerda;

**c)** O Título &lt;h2> deve possuir o plano de fundo com o valor `unset`;

**d)** Os Hiperlinks em &lt;h2> e que os que possuem a classe `topo` devem possuir a cor de texto branca;
