---
{
  "projection_kind": "taulib_declaration",
  "title": "temporal_ordering_from_persistence",
  "permalink": "/corpus/taulib/docs/book-vii-meta-registers/temporal-ordering-from-persistence/",
  "summary_short": "`theorem` declaration in `TauLib.BookVII.Meta.Registers`.",
  "declaration_id": "TauLib.BookVII.Meta.Registers::temporal_ordering_from_persistence",
  "declaration_slug": "temporal-ordering-from-persistence",
  "kind": "theorem",
  "name": "temporal_ordering_from_persistence",
  "module_name": "TauLib.BookVII.Meta.Registers",
  "module_url": "/corpus/taulib/docs/book-vii-meta-registers/",
  "source_line_start": 789,
  "source_line_end": 792,
  "registry_ids": [
    "VII.P06"
  ],
  "related_registry_items": [
    {
      "id": "VII.P06",
      "title": "Temporal Ordering from Persistence",
      "url": "/registry/object/VII.P06/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L789-L792",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Meta.Registers",
        "url": "/corpus/taulib/docs/book-vii-meta-registers/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L789-L792",
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

- Module: [TauLib.BookVII.Meta.Registers](/corpus/taulib/docs/book-vii-meta-registers/)
- Source path: [`TauLib/BookVII/Meta/Registers.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L789-L792)
- Source range: L789-L792
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `VII.P06` — Temporal Ordering from Persistence

## Immediate Comment / Docstring

```lean
/-- [VII.P06] Temporal Ordering from Persistence (ch24). Time is not
    assumed but derived: temporal ordering emerges from the persistence
    of NF-addresses through morphism chains. Directed morphisms
    induce a partial order = temporal sequence. -/
```

## Source Excerpt

```lean
theorem temporal_ordering_from_persistence :
    causation.factorization = true ∧
    causation.kernel_constrained = true :=
  ⟨rfl, rfl⟩
```
