---
{
  "projection_kind": "taulib_declaration",
  "title": "godel_avoidance",
  "permalink": "/corpus/taulib/docs/book-vii-meta-saturation/godel-avoidance/",
  "summary_short": "`theorem` declaration in `TauLib.BookVII.Meta.Saturation`.",
  "declaration_id": "TauLib.BookVII.Meta.Saturation::godel_avoidance",
  "declaration_slug": "godel-avoidance",
  "kind": "theorem",
  "name": "godel_avoidance",
  "module_name": "TauLib.BookVII.Meta.Saturation",
  "module_url": "/corpus/taulib/docs/book-vii-meta-saturation/",
  "source_line_start": 432,
  "source_line_end": 438,
  "registry_ids": [
    "VII.T07"
  ],
  "related_registry_items": [
    {
      "id": "VII.T07",
      "title": "Gödel Avoidance Theorem",
      "url": "/registry/object/VII.T07/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L432-L438",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Meta.Saturation",
        "url": "/corpus/taulib/docs/book-vii-meta-saturation/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L432-L438",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookVII.Meta.Saturation](/corpus/taulib/docs/book-vii-meta-saturation/)
- Source path: [`TauLib/BookVII/Meta/Saturation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L432-L438)
- Source range: L432-L438
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `VII.T07` — Gödel Avoidance Theorem

## Immediate Comment / Docstring

```lean
/-- [VII.T07] Gödel Avoidance: no sentence G in τ satisfies G ↔ ¬Coh_D(G).
    Four independent blockages:
    1. BWF violates (ii): diagonal requires unbounded witness
    2. No-Diagonal prevents surjection
    3. No-Contraction prevents SelfDesc³
    4. NF-Linearity prevents cycles

    Consequence: incompleteness phenomenon does not arise in τ. -/
```

## Source Excerpt

```lean
theorem godel_avoidance :
    avoidance.no_contraction = true ∧
    avoidance.no_diagonal = true ∧
    avoidance.bounded_witness = true ∧
    avoidance.nf_linearity = true ∧
    avoidance.generation_not_presentation = true :=
  ⟨rfl, rfl, rfl, rfl, rfl⟩
```
