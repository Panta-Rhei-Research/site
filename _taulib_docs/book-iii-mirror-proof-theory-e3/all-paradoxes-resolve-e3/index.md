---
{
  "projection_kind": "taulib_declaration",
  "title": "all_paradoxes_resolve_e3",
  "permalink": "/verify/taulib/docs/book-iii-mirror-proof-theory-e3/all-paradoxes-resolve-e3/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Mirror.ProofTheoryE3`.",
  "declaration_id": "TauLib.BookIII.Mirror.ProofTheoryE3::all_paradoxes_resolve_e3",
  "declaration_slug": "all-paradoxes-resolve-e3",
  "kind": "theorem",
  "name": "all_paradoxes_resolve_e3",
  "module_name": "TauLib.BookIII.Mirror.ProofTheoryE3",
  "module_url": "/verify/taulib/docs/book-iii-mirror-proof-theory-e3/",
  "source_line_start": 356,
  "source_line_end": 357,
  "registry_ids": [
    "III.D75"
  ],
  "related_registry_items": [
    {
      "id": "III.D75",
      "title": "E₂→E₃ Boundary Crossing",
      "url": "/registry/object/III.D75/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/ProofTheoryE3.lean#L356-L357",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/ProofTheoryE3.lean#L356-L357",
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
- Source path: [`TauLib/BookIII/Mirror/ProofTheoryE3.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/ProofTheoryE3.lean#L356-L357)
- Source range: L356-L357
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.D75` — E₂→E₃ Boundary Crossing

## Immediate Comment / Docstring

```lean
/-- [III.D75] Structural: all paradoxes resolve at E3. -/
```

## Source Excerpt

```lean
theorem all_paradoxes_resolve_e3 :
    all_paradoxes.all (fun p => p.resolution_level == .E3) = true := by native_decide
```
