---
{
  "projection_kind": "taulib_declaration",
  "title": "yoneda_code_roundtrip",
  "permalink": "/verify/taulib/docs/book-ii-central-theorem-yoneda-applied/yoneda-code-roundtrip/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.CentralTheorem.YonedaApplied`.",
  "declaration_id": "TauLib.BookII.CentralTheorem.YonedaApplied::yoneda_code_roundtrip",
  "declaration_slug": "yoneda-code-roundtrip",
  "kind": "theorem",
  "name": "yoneda_code_roundtrip",
  "module_name": "TauLib.BookII.CentralTheorem.YonedaApplied",
  "module_url": "/verify/taulib/docs/book-ii-central-theorem-yoneda-applied/",
  "source_line_start": 308,
  "source_line_end": 313,
  "registry_ids": [
    "II.L14"
  ],
  "related_registry_items": [
    {
      "id": "II.L14",
      "title": "Yoneda Application",
      "url": "/registry/object/II.L14/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/YonedaApplied.lean#L308-L313",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/YonedaApplied.lean#L308-L313",
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
- Source path: [`TauLib/BookII/CentralTheorem/YonedaApplied.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/YonedaApplied.lean#L308-L313)
- Source range: L308-L313
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.L14` — Yoneda Application

## Immediate Comment / Docstring

```lean
/-- [II.L14] Pre-Yoneda embedding of the identity is recovered by Code.
    code_extract(preyoneda(id), k, x) = preyoneda(id)(x, k)
    Both sides equal reduce(x, k). -/
```

## Source Excerpt

```lean
theorem yoneda_code_roundtrip (x k : TauIdx) :
    code_extract (fun n => (preyoneda_embed_nat (fun m => m) n k : Int)) k x =
    (preyoneda_embed_nat (fun m => m) x k : Int) := by
  simp only [code_extract, preyoneda_embed_nat, reduce]
  congr 1
  exact Nat.mod_mod_of_dvd x (dvd_refl (primorial k))
```
