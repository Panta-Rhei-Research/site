---
{
  "projection_kind": "taulib_declaration",
  "title": "enrichment_strict",
  "permalink": "/verify/taulib/docs/book-iii-hinge-hinge-theorem/enrichment-strict/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Hinge.HingeTheorem`.",
  "declaration_id": "TauLib.BookIII.Hinge.HingeTheorem::enrichment_strict",
  "declaration_slug": "enrichment-strict",
  "kind": "theorem",
  "name": "enrichment_strict",
  "module_name": "TauLib.BookIII.Hinge.HingeTheorem",
  "module_url": "/verify/taulib/docs/book-iii-hinge-hinge-theorem/",
  "source_line_start": 360,
  "source_line_end": 364,
  "registry_ids": [
    "III.T41"
  ],
  "related_registry_items": [
    {
      "id": "III.T41",
      "title": "Hinge Theorem",
      "url": "/registry/object/III.T41/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Hinge/HingeTheorem.lean#L360-L364",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Hinge.HingeTheorem",
        "url": "/verify/taulib/docs/book-iii-hinge-hinge-theorem/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Hinge/HingeTheorem.lean#L360-L364",
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

- Module: [TauLib.BookIII.Hinge.HingeTheorem](/verify/taulib/docs/book-iii-hinge-hinge-theorem/)
- Source path: [`TauLib/BookIII/Hinge/HingeTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Hinge/HingeTheorem.lean#L360-L364)
- Source range: L360-L364
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.T41` — Hinge Theorem

## Immediate Comment / Docstring

```lean
/-- [III.T41] Structural: enrichment level ordering is strict. -/
```

## Source Excerpt

```lean
theorem enrichment_strict :
    EnrLevel.lt .E0 .E1 = true /\
    EnrLevel.lt .E1 .E2 = true /\
    EnrLevel.lt .E2 .E3 = true := by
  exact ⟨rfl, rfl, rfl⟩
```
