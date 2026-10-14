# Atendimento com propósito

[Explorar o estudo de caso](https://acnpacheco.github.io/portfolio-design-instrucional/#case)

Empresa e situações fictícias. O caso conecta diagnóstico, objetivos observáveis, storyboard, quatro decisões com feedback e plano de avaliação no trabalho.

## Entregas

- `dist/assets/case/`: diagnóstico, planejamento, storyboard, roteiro audiovisual, protocolo de validação e plano de avaliação.
- `dist/course/`: experiência interativa. Quatro decisões, 25 pontos cada; aprovação a partir de 75/100. O modo demonstrativo salva o progresso no navegador.
- `dist/assets/scorm/`: pacotes demonstrativos SCORM 1.2 e SCORM 2004 4th Edition, para importação no LMS.

## Reconstruir e verificar

```text
node scripts/check-scorm.cjs
python scripts/build-scorm.py
```

O empacotador confere XML, referências de arquivos e integridade ZIP. Os testes de comunicação usam adaptadores simulados para inicialização, aprovação, reprovação, retomada e encerramento.

## Limites

Não há validação em LMS real nem certificação de conformidade. Importação, retomada e relatórios precisam ser testados no ambiente de destino. O roteiro audiovisual está pronto; áudio/vídeo ainda não foram produzidos. Revisão formal de acessibilidade e testes com usuários pendentes.

O curso não alimenta automaticamente os KPIs do painel. A execução pode ser registrada manualmente ou por Excel. Nenhum resultado de aprendizagem ou impacto real é atribuído ao estudo.

Referência técnica: https://scorm.com/scorm-explained/technical-scorm/run-time/
