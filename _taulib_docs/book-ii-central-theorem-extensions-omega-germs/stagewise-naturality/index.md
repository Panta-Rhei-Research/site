---
{
  "projection_kind": "taulib_declaration",
  "title": "stagewise_naturality",
  "permalink": "/verify/taulib/docs/book-ii-central-theorem-extensions-omega-germs/stagewise-naturality/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.CentralTheorem.ExtensionsOmegaGerms`.",
  "declaration_id": "TauLib.BookII.CentralTheorem.ExtensionsOmegaGerms::stagewise_naturality",
  "declaration_slug": "stagewise-naturality",
  "kind": "theorem",
  "name": "stagewise_naturality",
  "module_name": "TauLib.BookII.CentralTheorem.ExtensionsOmegaGerms",
  "module_url": "/verify/taulib/docs/book-ii-central-theorem-extensions-omega-germs/",
  "source_line_start": 290,
  "source_line_end": 294,
  "registry_ids": [
    "II.L13"
  ],
  "related_registry_items": [
    {
      "id": "II.L13",
      "title": "Stagewise Naturality",
      "url": "/registry/object/II.L13/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/ExtensionsOmegaGerms.lean#L290-L294",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.CentralTheorem.ExtensionsOmegaGerms",
        "url": "/verify/taulib/docs/book-ii-central-theorem-extensions-omega-germs/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/ExtensionsOmegaGerms.lean#L290-L294",
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

- Module: [TauLib.BookII.CentralTheorem.ExtensionsOmegaGerms](/verify/taulib/docs/book-ii-central-theorem-extensions-omega-germs/)
- Source path: [`TauLib/BookII/CentralTheorem/ExtensionsOmegaGerms.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/ExtensionsOmegaGerms.lean#L290-L294)
- Source range: L290-L294
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.L13` — Stagewise Naturality

## Immediate Comment / Docstring

```lean
/-- [II.L13] Stagewise naturality (structural): reduce(bndlift(x, k+1), k) = reduce(x, k).
    Since bndlift(x, k+1) = reduce(x, k+2) and k <= k+2, this follows
    from reduction_compat. -/
```

## Source Excerpt

```lean
theorem stagewise_naturality (x k : TauIdx) :
    reduce (bndlift x (k + 1)) k = reduce x k := by
  simp only [bndlift, reduce]
  have h : k ≤ k + 1 + 1 := Nat.le_add_right k 2
  exact Nat.mod_mod_of_dvd x (primorial_dvd h)
```
