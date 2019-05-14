# Analisando uma Página da Web

Ao acessar uma página Web, como a do [IFPB](http://www.ifpb.edu.br/), percebemos que muitos detalhes e conteúdos são estruturadas para criar um site.

Além disso, devido a natureza da Web, geralmente, os arquivos que visualizamos nos navagadores dos sites são cópias geradas em servidores disponívies na Internet, e que portanto, podem ser analisadas para se compreender a forma como as páginas são criadas.

Mas ao acessar os arquivos com os navegadores, quase sempre surge uma pergunta inevitável, principalmente quando se começar a estudar sites, quais são as formas mais acessíveis de ser analisar o código fonte de uma página Web?

Para responder essa questão é preciso entender que a maioria das alternativas se dá por meio do navegador, ao acessar a própria página. Um exemplo disso, pode ser visto na *Figura 1* ao acessar uma página do [IFPB](http://www.ifpb.edu.br/) usando o Google Chrome, pois no item **Ver Código Fonte** do menu popup, é possível ver que outra janela é aberta com o código fonte utilizado para construir a página.

*Figura 1* - Página do IFPB.
![Página do IFPB](screen-ifpb.png)

Ao percorrer esse arquivo, conseguimos ver o código fonte utilizado para criar as estruturas da página. Junto com o arquivo, também se identificar vários outros arquivos usados na página, como imagens (.png), estilos (.css) e javascript (.js).

Outra alternativa de analisar o códifo fonte de uma página Web pode ser usando a **Ferramenta de Desenvolvedor** dos navegadores. A *Figura 2* ilustra como ela pode ser exibida no Google Chrome, logo abaixo da exibição da página.

*Figura 2* - Ferramenta do Desenvolvedor.
![Ferramenta do Desenvolvedor](screen-devtool.png)

Um modo bastante fácil de acessar essa ferramenta é através do menu popup, por exemplo, para saber como é a estrutura do HTML do título IFPB, visível na *Figura 2*, basta ativar o item **Inspecionar Elemento** menu popup, sob o título.

Perceba que tal ação evidencia na ferramenta, o código, e no site, o título. O que nos permite concluir que a linha reponsável por exibir o título é:

```
<h1 id="portal-title" class="corto">IFPB</h1>
```

Por fim, outro recurso que pode ser atrelado ao navegador, para auxilar na análise do código fonte de uma página Web, seria o uso do **[Plugin Web Developer](https://chrome.google.com/webstore/detail/web-developer/bfbameneiokkgbdmiekhjnmfkcnldhhm)** que é disponível na maioria dos navegadores.

Com esse plugin é possível isolar a estrutura do estilo da página, além de interroper a execução das ações e animações de uma página, por exemplo, a *Figura 3* exibe a página do IFPB sem nenhum estilo.

*Figura 3* - Plugin Web Developer.
![Plugin Web Developer](screen-plugin.png)

Um fato importante que pode ser visto na *Figura 3*, é que através da ocultação do estilo, fica claro identificar o seu papel numa página Web, pois foi com uso do estilo que a página do IFPB conseguiu configurar a forma como as estruturas (parágrafos, títulos, hyperlink, formulários, imagens, etc) seriam exibidas.

Um exemplo perceptível são os hyperlinks, sem o estilo eles se apresenta da forma clássica, em azul e com sublinhado, já com estilo as cores são personalizadas e o sublinhado é removido.

Portanto, como foi descrito, as opções de **Ver Código Fonte**, **Ferramenta de Desenvolvedor** e **Plugin Web Developer** facilitam o acesso ao código fonte das páginas Web. Então tente explorá-las na página do [IFPB](http://www.ifpb.edu.br/), e em mais duas páginas da Internet.
