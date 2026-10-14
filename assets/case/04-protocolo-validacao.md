# Protocolo de validação — Atendimento com propósito

Pacotes de demonstração SCORM 1.2 e SCORM 2004 4th Edition. Não certificados. Data de preparação: 14/10/2026.

## Verificações locais

- Manifesto XML na raiz de cada ZIP, organização, item e recurso de lançamento.
- Arquivos locais referenciados presentes no pacote.
- SCORM 1.2: LMSInitialize, LMSGetValue, LMSSetValue, LMSCommit e LMSFinish.
- SCORM 2004: Initialize, GetValue, SetValue, Commit e Terminate.
- Gravação de local de retomada, dados de suspensão, nota, resultado e tempo de sessão.
- Testes automatizados com adaptadores simulados para aprovação, reprovação, retomada e falha de inicialização.
- Checagem visual e interação no navegador.

Essas verificações não substituem testes de interoperabilidade, validação integral contra esquemas ou uma suíte de conformidade.

## Matriz de teste no LMS — PENDENTE

Registrar para cada teste: data, pessoa responsável, LMS e versão, navegador, versão SCORM, resultado esperado, resultado observado, evidência e defeito associado.

| Teste | Procedimento | Resultado esperado | Estado |
|---|---|---|---|
| Importação | Importar cada ZIP em ambiente de teste | Curso identificado e sem erro de importação | Pendente |
| Lançamento | Abrir pelo LMS | Inicialização confirmada, conteúdo legível | Pendente |
| Retomada | Responder parte, fechar, reabrir | Retomar sem perder respostas confirmadas | Pendente |
| Aprovação | Acertar 3 ou 4 decisões | Nota 75 ou 100 e aprovação no relatório | Pendente |
| Reprovação | Acertar até 2 decisões | Nota até 50 e reprovação no relatório | Pendente |
| Conclusão | Finalizar as quatro decisões | 2004: completed separado de passed/failed; 1.2: passed/failed | Pendente |
| Tempo e encerramento | Abrir, interagir e sair | Sessão registrada e encerrada sem duplicidade | Pendente |
| Nova tentativa | Usar recurso do LMS | Política de tentativas aplicada sem sobrescrever indevidamente | Pendente |
| Relatórios | Consultar dados do curso | Nota e status coerentes com a tentativa | Pendente |
| Acessibilidade | Teclado, leitor de tela e zoom | Conteúdo e controles utilizáveis | Pendente |

## Limites e dados

Sem integração automática entre curso e painel. O painel recebe execução manualmente ou por Excel. O modo demonstrativo salva progresso no navegador; os pacotes precisam da API do LMS para confirmar registro.

Referências técnicas: https://scorm.com/scorm-explained/technical-scorm/run-time/ e https://scorm.com/scorm-explained/technical-scorm/run-time/run-time-reference/
