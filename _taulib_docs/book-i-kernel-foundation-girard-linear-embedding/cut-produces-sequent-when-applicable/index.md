---
{
  "projection_kind": "taulib_declaration",
  "title": "cut_produces_sequent_when_applicable",
  "permalink": "/verify/taulib/docs/book-i-kernel-foundation-girard-linear-embedding/cut-produces-sequent-when-applicable/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.KernelFoundation.GirardLinearEmbedding`.",
  "declaration_id": "TauLib.BookI.KernelFoundation.GirardLinearEmbedding::cut_produces_sequent_when_applicable",
  "declaration_slug": "cut-produces-sequent-when-applicable",
  "kind": "theorem",
  "name": "cut_produces_sequent_when_applicable",
  "module_name": "TauLib.BookI.KernelFoundation.GirardLinearEmbedding",
  "module_url": "/verify/taulib/docs/book-i-kernel-foundation-girard-linear-embedding/",
  "source_line_start": 224,
  "source_line_end": 231,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/KernelFoundation/GirardLinearEmbedding.lean#L224-L231",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.KernelFoundation.GirardLinearEmbedding",
        "url": "/verify/taulib/docs/book-i-kernel-foundation-girard-linear-embedding/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/verify/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/KernelFoundation/GirardLinearEmbedding.lean#L224-L231",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
    }
  },
  "layout": "taulib-doc",
  "lane": "verify",
  "v2_lane": "verify",
  "status": "Canonical",
  "generated_from": "corpus/taulib-projections",
  "projection_version": "v0.1",
  "canonical_source": "Panta-Rhei-Research/taulib",
  "do_not_edit": true,
  "type": "TauLib Declaration"
}
---

## Declaration Projection

This page is generated directly from the pinned TauLib Lean source snapshot. The source excerpt is public because the active TauLib repository is public.

## Source Provenance

- Module: [TauLib.BookI.KernelFoundation.GirardLinearEmbedding](/verify/taulib/docs/book-i-kernel-foundation-girard-linear-embedding/)
- Source path: [`TauLib/BookI/KernelFoundation/GirardLinearEmbedding.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/KernelFoundation/GirardLinearEmbedding.lean#L224-L231)
- Source range: L224-L231
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Paper §3 cut-elimination Hauptsatz statement (statement-level
    form)**.

    Every proof with cut can be transformed into a cut-free proof,
    and the cut-free NF is unique up to inessential permutations.

    Rendered as a Prop-level claim that the cut operation, when
    applicable, produces a sequent — matching the paper's framing
    scope (structural witness, not formal proof system).

    Full machine-checked cut-elimination + uniqueness is deferred
    to Book III per `rem:scope-structural`. -/
```

## Source Excerpt

```lean
theorem cut_produces_sequent_when_applicable
    (s1 s2 : Sequent) (a : Formula)
    (h1 : s1.succedent = [a])
    (h2 : s2.antecedent.head? = some a) :
    ∃ s : Sequent, cutSequent s1 s2 a = some s := by
  refine ⟨⟨s1.antecedent ++ s2.antecedent.tail, s2.succedent⟩, ?_⟩
  unfold cutSequent
  simp [h1, h2]
```
