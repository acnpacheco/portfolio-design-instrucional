# Forma — Portfólio de Design Instrucional

Primeira versão visual de um portfólio de processos, com experiência de painel SaaS. Os estudos de caso são fictícios e não representam resultados profissionais obtidos.

## Abrir

Abra `dist/index.html` em um navegador ou sirva a pasta `dist` com um servidor estático. Não requer instalação de dependências.

## Recursos

- Visão geral e projetos; criação de projetos locais.
- LNT editável e salva no navegador.
- Kanban com movimentação por seletor e conclusão de tarefas.
- Competências e plano de medição de KPIs.

## Limites atuais

Os dados são armazenados apenas no navegador. Não há contas, sincronização entre dispositivos ou integração automática com LMS. Pacotes SCORM demonstrativos estão disponíveis, mas ainda precisam de validação no LMS de destino. Não é ainda um SaaS de produção.

## Próximas entregas

1. Personalizar autoria e posicionamento profissional.
2. Revisar o estudo de caso com especialista e público representativo.
3. Validar os pacotes SCORM 1.2 e 2004 em LMS real.
4. Gravar e editar áudio/vídeo a partir do roteiro disponível.
5. Completar revisão formal de acessibilidade e teste com leitor de tela.

## Progresso do escopo geral

85% estimados: painel, orçamento, entrada manual/Excel, execução, estudo de caso, curso interativo e pacotes preparados. Validação em LMS, produção audiovisual e revisão formal de acessibilidade pendentes. Percentuais dos cartões são exemplos independentes.

## Orçamento por área
Verba anual, pagamentos e reservas por treinamento. Disponível = aprovado - pago - a pagar. Valores demonstrativos, editáveis e salvos somente no navegador. Inclui filtros por ano/área, alertas de saldo negativo, impressão e exportação CSV.

Referências: [ATD 2026](https://www.td.org/content/atd-blog/2026-state-of-the-industry-report-indicates-latest-td-trends) e [CIPD](https://www.cipd.org/uk/knowledge/factsheets/evaluating-learning-factsheet/).


## Setores, execução e Excel
- Cadastre um setor com sua verba anual em Orçamento de T&D.
- Registre status, responsável, prazo, LNT, inscritos, presentes, concluintes, duração, satisfação e aplicação no trabalho.
- Execução de treinamentos mostra gráficos e cobertura das medições; células vazias não são tratadas como zero.
- Dados & Excel permite baixar um modelo fictício e exportar/importar arquivos .xlsx com as abas Setores e Treinamentos.
- A importação valida todas as linhas antes de gravar. Mesmo ID atualiza; novo ID acrescenta. Registros ausentes não são excluídos.
- Até 5 MB e 2.000 linhas por aba. Preservar os cabeçalhos do modelo. As planilhas originais de outras estruturas precisam ser adaptadas ao modelo.
- SheetJS CE 0.20.3 distribuído localmente; licença em dist/vendor/SheetJS-LICENSE.txt.

Verificação: cálculos de orçamento, filtros, saldo negativo, importação com atualização sem duplicação, indicadores, datas inválidas, limites de contagem e ausência versus zero.


## Qualidade e acessibilidade
O módulo Qualidade & validação mantém um checklist separado para SCORM 1.2 e 2004. Todos os testes em LMS começam pendentes. Resultados Aprovado/Falhou exigem plataforma e observação. Os registros ficam neste navegador e podem ser exportados em JSON. Melhorias de teclado, foco, rótulos, tabelas e contraste estão descritas em dist/assets/case/06-revisao-acessibilidade.md. Revisão com leitor de tela e validação no LMS real continuam pendentes.

