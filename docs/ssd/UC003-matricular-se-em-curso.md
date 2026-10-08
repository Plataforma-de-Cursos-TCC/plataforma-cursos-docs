# UC003 — Matricular-se em Curso

Diagrama de sequência do sistema para o caso de uso UC003 (Matricular-se em Curso). Representa o fluxo de consulta do curso pelo Aluno, verificação de matrícula prévia, processamento do pagamento simulado e confirmação de matrícula.

<!-- revisar: diagrama reconstruído a partir da descrição da v11 (na v11 é só imagem); conferir contra a figura original. -->
```mermaid
sequenceDiagram
    actor Aluno
    participant CursoView as Front-end web
    participant MatriculaController as API
    participant DB as Banco de Dados

    Aluno->>CursoView: acessa página de um curso
    CursoView->>MatriculaController: obterCurso(cursoId)
    MatriculaController->>DB: sp_Buscar_Curso
    DB-->>MatriculaController: dados do curso
    alt curso publicado e aluno não matriculado
        MatriculaController-->>CursoView: exibe botão "Matricular-se"
        Aluno->>CursoView: clica em "Matricular-se"
        CursoView->>MatriculaController: matricular(alunoId, cursoId)
        MatriculaController->>DB: sp_Processar_Pagamento_Simulado
        DB-->>MatriculaController: pagamento confirmado
        MatriculaController->>DB: sp_Criar_Matricula
        DB-->>MatriculaController: matrícula registrada
        MatriculaController-->>CursoView: matrícula confirmada
        CursoView-->>Aluno: curso aparece em "Meus Cursos"
    else aluno já matriculado
        MatriculaController-->>CursoView: já matriculado
        CursoView-->>Aluno: exibe botão "Continuar assistindo"
    else curso em rascunho (não publicado)
        MatriculaController-->>CursoView: erro - curso não encontrado
        CursoView-->>Aluno: exibe erro de curso não encontrado
    end
```
