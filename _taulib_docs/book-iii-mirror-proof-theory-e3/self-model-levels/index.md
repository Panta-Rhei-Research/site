---
{
  "projection_kind": "taulib_declaration",
  "title": "self_model_levels",
  "permalink": "/verify/taulib/docs/book-iii-mirror-proof-theory-e3/self-model-levels/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Mirror.ProofTheoryE3`.",
  "declaration_id": "TauLib.BookIII.Mirror.ProofTheoryE3::self_model_levels",
  "declaration_slug": "self-model-levels",
  "kind": "theorem",
  "name": "self_model_levels",
  "module_name": "TauLib.BookIII.Mirror.ProofTheoryE3",
  "module_url": "/verify/taulib/docs/book-iii-mirror-proof-theory-e3/",
  "source_line_start": 348,
  "source_line_end": 349,
  "registry_ids": [
    "III.D74"
  ],
  "related_registry_items": [
    {
      "id": "III.D74",
      "title": "Diagrammatic Sector of E₃",
      "url": "/registry/object/III.D74/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/ProofTheoryE3.lean#L348-L349",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Mirror.ProofTheoryE3",
        "url": "/verify/taulib/docs/book-iii-mirror-proof-theory-e3/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/ProofTheoryE3.lean#L348-L349",
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

- Module: [TauLib.BookIII.Mirror.ProofTheoryE3](/verify/taulib/docs/book-iii-mirror-proof-theory-e3/)
- Source path: [`TauLib/BookIII/Mirror/ProofTheoryE3.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/ProofTheoryE3.lean#L348-L349)
- Source range: L348-L349
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.D74` — Diagrammatic Sector of E₃

## Immediate Comment / Docstring

```lean
/-- [III.D74] Structural: self-model functor goes from E2 to E3. -/
```

## Source Excerpt

```lean
theorem self_model_levels :
    EnrLevel.lt .E2 .E3 = true := rfl
```
