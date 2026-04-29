---
{
  "projection_kind": "taulib_declaration",
  "title": "nf_addr_10_1",
  "permalink": "/verify/taulib/docs/book-iii-physics-hodge/nf-addr-10-1/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Physics.Hodge`.",
  "declaration_id": "TauLib.BookIII.Physics.Hodge::nf_addr_10_1",
  "declaration_slug": "nf-addr-10-1",
  "kind": "theorem",
  "name": "nf_addr_10_1",
  "module_name": "TauLib.BookIII.Physics.Hodge",
  "module_url": "/verify/taulib/docs/book-iii-physics-hodge/",
  "source_line_start": 290,
  "source_line_end": 293,
  "registry_ids": [
    "III.T28"
  ],
  "related_registry_items": [
    {
      "id": "III.T28",
      "title": "NF-Addressability Theorem",
      "url": "/registry/object/III.T28/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/Hodge.lean#L290-L293",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Physics.Hodge",
        "url": "/verify/taulib/docs/book-iii-physics-hodge/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/Hodge.lean#L290-L293",
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

- Module: [TauLib.BookIII.Physics.Hodge](/verify/taulib/docs/book-iii-physics-hodge/)
- Source path: [`TauLib/BookIII/Physics/Hodge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/Hodge.lean#L290-L293)
- Source range: L290-L293
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.T28` — NF-Addressability Theorem

## Immediate Comment / Docstring

```lean
/-- [III.T28] Structural: NF-addressability at depth 1. -/
```

## Source Excerpt

```lean
theorem nf_addr_10_1 :
    nf_addressability_check 10 1 = true := by native_decide

end Tau.BookIII.Physics
```
