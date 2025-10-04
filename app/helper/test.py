from app.helper.geminiAI import classifyEmailContent
from deepSeekApi import deepSeekClassifyEmailContent

email = f"""
Prezado(a) estudante, A avaliação socioeconômica do seu contexto familiar foi concluída e você foi aprovado(a) para acesso aos programas de assistência estudantil na categoria B. Para consultar o período de validade de sua avaliação socioeconômica, acesse o Cadastro para Programas de Assistência Estudantil (CPAE) na plataforma Minha UFOP. Conforme a Resolução CUNI/UFOP no 1380, de 26/04/2012, é facultado ao estudante classificado na categoria B o acesso aos programas de bolsa alimentação integral e bolsa permanência com valores parciais (75%). A avaliação socioeconômica também pode ser utilizada para pleitear vagas nas moradias da UFOP, modalidade socioeconômica, mediante inscrição e aprovação nos editais vigentes. Para conferir os editais disponíveis acesse: http://www.prace.ufop.br. Maiores informações estão disponíveis no site da Prace: www.prace.ufop.br. Acesse também o tópico de Perguntas Frequentes: http://www.prace.ufop.br/%3Cnolink%3E/avaliacao-socioeconomica. Não conseguindo esclarecer suas dúvidas por esses canais entre em contato pelo e-mail faleconosco.prace@ufop.edu.br Atenciosamente, Pró-Reitoria de Assuntos Comunitários e Estudantis
...Ontem, estive na Polícia Federal em Belo Horizonte para solicitar a autorização de residência temporária para nacionais da CPLP. No entanto, durante a triagem documental, mesmo tendo apresentado todos os documentos exigidos pela Portaria Interministerial MJSP/MRE nº 40, de 1º de setembro de 2023, fui informado de que a apresentação dos antecedentes criminais do meu país de origem era obrigatória.

Contudo, a referida portaria estabelece que:

IV - Certidão de antecedentes criminais ou documento equivalente, emitido pela autoridade competente no país de origem ou nos países em que houver residido nos últimos cinco anos, devidamente legalizada ou apostilada, se produzido no exterior.

Considerando que resido no Brasil ininterruptamente desde maio de 2018 (há aproximadamente sete anos), entendo que minha obrigação seria apresentar apenas os antecedentes criminais do Brasil, conforme o trecho destacado acima.

Além disso, ao conversar com colegas que chegaram ao Brasil no mesmo período que eu e que realizaram esse mesmo procedimento em outros estados, fui informado de que não lhes foi exigida a apresentação dos antecedentes criminais do país de origem.

Outro ponto importante é que a obtenção desse documento na Guiné-Bissau só pode ser feita presencialmente no Ministério da Justiça. Não há possibilidade de solicitá-lo pela internet ou por outro meio remoto, o que significa que eu precisaria de alguém no país para fazer a solicitação e, posteriormente, enviá-lo ao Brasil por correio internacional. Isso torna o processo significativamente mais demorado.

Diante disso, gostaria de esclarecer se há, de fato, alguma exigência específica para a unidade de Belo Horizonte ou se houve um equívoco na triagem documental.

Agradeço a atenção e aguardo um retorno.

Atenciosamente,

"""
resp = deepSeekClassifyEmailContent(email)

print(resp)