# UC003 — Matricular-se em Curso

Diagrama de sequência do sistema para o caso de uso UC003 (Matricular-se em Curso). Representa o fluxo de consulta do curso pelo Aluno, verificação de matrícula prévia, processamento do pagamento simulado e confirmação de matrícula.

```mermaid
sequenceDiagram
    actor Aluno
    participant CursoView
    participant MatriculaController
    participant Banco de Dados

    Aluno->>CursoView: acessa página de um curso
    CursoView->>+MatriculaController: obterCurso(cursoId)
    MatriculaController->>+Banco de Dados: sp_Buscar_Curso
    Banco de Dados-->>-MatriculaController: dados do curso
    alt curso publicado e aluno não matriculado
        MatriculaController-->>CursoView: exibe botão "matricular-se"
        deactivate MatriculaController
        Aluno->>CursoView: clica em "matricular-se"
        CursoView->>+MatriculaController: matricular(alunoId, cursoId)
        MatriculaController->>+Banco de Dados: sp_Processar_Pagamento_Simulado
        Banco de Dados-->>-MatriculaController: pagamento confirmado
        MatriculaController->>+Banco de Dados: sp_Criar_Matricula
        Banco de Dados-->>-MatriculaController: matrícula registrada
        MatriculaController-->>CursoView: matrícula confirmada
        deactivate MatriculaController
        CursoView-->>Aluno: curso aparece em "meus cursos"
    else aluno já matriculado
        MatriculaController-->>CursoView: já matriculado
        CursoView-->>Aluno: exibe botão "continuar assistindo"
    else curso em rascunho (não publicado)
        MatriculaController-->>CursoView: erro — curso não encontrado
        CursoView-->>Aluno: exibe erro de curso não encontrado
    end
```
