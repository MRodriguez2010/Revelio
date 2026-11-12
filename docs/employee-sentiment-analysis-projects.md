# Employee Sentiment Analysis project guide

Start with [Revelio](https://github.com/MRodriguez2010/Revelio) for the interactive comparison, screenshots, and example PowerPoint. This guide connects the public projects by the analyst task they demonstrate.

## Explore the project family

| Project | Focus | What to inspect |
| --- | --- | --- |
| [Revelio](https://github.com/MRodriguez2010/Revelio) | Interactive comparison | Configure a focus company, peers, and quarters; inspect the calculation and export an editable PowerPoint. |
| [Employee Sentiment Analysis Toolkit](https://github.com/MRodriguez2010/ESA_Toolkit-public) | Workbook intake | Validate required fields, aggregate answer counts, bounds, and duplicate keys before exporting CSV. |
| [Employee Sentiment Analysis Core Pipeline](https://github.com/MRodriguez2010/ESA-Core-Pipeline-public) | Batch reporting | Generate a peer comparison and editable deck from validated aggregate survey counts. |
| [Employee Sentiment Analysis Evidence Curation](https://github.com/MRodriguez2010/ESA-Ai-public) | Evidence curation | Propose a topic narrative and require hash-bound approval; an optional local model can select an evidence ID. |
| [Voice Lab](https://github.com/MRodriguez2010/talent-solutions-voice-lab-public) | Analyst review | Inspect evidence, approve topics in a local workbench, and export only the approved slides. |
| [workforce-survey-reporting](https://github.com/MRodriguez2010/workforce-survey-reporting) | Survey measurement | Use Python and SQL to compare two survey waves, with minimum group sizes and percentage-point reporting. |
| [Dashboard-Products-public](https://github.com/MRodriguez2010/Dashboard-Products-public) | Dashboard exploration | Explore employee-review sentiment and topic scoring alongside other business analytics demos. |
| [PPTX_TemplateUpdate-public](https://github.com/MRodriguez2010/PPTX_TemplateUpdate-public) | Presentation maintenance | Detect and map anchors between PowerPoint templates, then verify the generated output. |
| [NetDump-public](https://github.com/MRodriguez2010/NetDump-public) | Research diagnostics | Inspect privacy-conscious network summaries and the documented historical public-source index. |
| [Mermaid_Swimlanes_Editor-public](https://github.com/MRodriguez2010/Mermaid_Swimlanes_Editor-public) | Workflow documentation | Edit process diagrams and inspect the included historical benchmark review workflow. |

## Suggested review path

1. **See the result.** Open Revelio's [interface](interface.png), [report preview](report-output.png), and [example deck](../examples/employee-sentiment-analysis.pptx).
2. **Trace the calculation.** Review Revelio's [analysis model](../reporting/model.py), then the [survey SQL](https://github.com/MRodriguez2010/workforce-survey-reporting/blob/main/sql/summary.sql) for the separate two-wave example.
3. **Explore repeatable delivery.** Review workbook intake, the batch pipeline, evidence curation, and Voice Lab's approval workflow.
4. **Inspect supporting tools.** Look at template migration, dashboards, research diagnostics, and workflow diagrams.

These are related standalone projects and public adaptations. The task sequence above explains their relationship; it does not claim that every repository is already integrated into one application. Follow each project's README for its supported input schema and run instructions.

## Understand the examples

Revelio and the core survey demonstrations use fictional organizations and synthetic response counts. Some companion repositories also contain separately labeled historical public ratings and benchmark slides with source notes. A five-point review-site rating is a different measure from a favorable-response percentage. Historical examples should be read with their capture dates and source limitations.

[Browse all public repositories with the employee-sentiment-analysis topic](https://github.com/search?q=user%3AMRodriguez2010+is%3Apublic+topic%3Aemployee-sentiment-analysis&type=repositories).
