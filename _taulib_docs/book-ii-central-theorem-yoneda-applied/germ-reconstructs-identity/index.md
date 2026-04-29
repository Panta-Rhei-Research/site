---
{
  "projection_kind": "taulib_declaration",
  "title": "germ_reconstructs_identity",
  "permalink": "/verify/taulib/docs/book-ii-central-theorem-yoneda-applied/germ-reconstructs-identity/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.CentralTheorem.YonedaApplied`.",
  "declaration_id": "TauLib.BookII.CentralTheorem.YonedaApplied::germ_reconstructs_identity",
  "declaration_slug": "germ-reconstructs-identity",
  "kind": "theorem",
  "name": "germ_reconstructs_identity",
  "module_name": "TauLib.BookII.CentralTheorem.YonedaApplied",
  "module_url": "/verify/taulib/docs/book-ii-central-theorem-yoneda-applied/",
  "source_line_start": 327,
  "source_line_end": 329,
  "registry_ids": [
    "II.T39"
  ],
  "related_registry_items": [
    {
      "id": "II.T39",
      "title": "Omega-Germs iff Holomorphic Functions",
      "url": "/registry/object/II.T39/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/YonedaApplied.lean#L327-L329",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.CentralTheorem.YonedaApplied",
        "url": "/verify/taulib/docs/book-ii-central-theorem-yoneda-applied/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/YonedaApplied.lean#L327-L329",
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

- Module: [TauLib.BookII.CentralTheorem.YonedaApplied](/verify/taulib/docs/book-ii-central-theorem-yoneda-applied/)
- Source path: [`TauLib/BookII/CentralTheorem/YonedaApplied.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/YonedaApplied.lean#L327-L329)
- Source range: L327-L329
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.T39` — Omega-Germs iff Holomorphic Functions

## Immediate Comment / Docstring

```lean
/-- [II.T39] Decode of the identity code table reconstructs reduce:
    decode_reconstruct(id_table, k, x) = reduce(x, k).
    This is the germ-to-holomorphic direction. -/
```

## Source Excerpt

```lean
theorem germ_reconstructs_identity (x k : TauIdx) :
    decode_reconstruct (fun a => (a : Int)) k x = (reduce x k : Int) := by
  simp [decode_reconstruct, reduce]
```
