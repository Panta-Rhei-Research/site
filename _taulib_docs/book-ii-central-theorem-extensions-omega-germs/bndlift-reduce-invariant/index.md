---
{
  "projection_kind": "taulib_declaration",
  "title": "bndlift_reduce_invariant",
  "permalink": "/verify/taulib/docs/book-ii-central-theorem-extensions-omega-germs/bndlift-reduce-invariant/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.CentralTheorem.ExtensionsOmegaGerms`.",
  "declaration_id": "TauLib.BookII.CentralTheorem.ExtensionsOmegaGerms::bndlift_reduce_invariant",
  "declaration_slug": "bndlift-reduce-invariant",
  "kind": "theorem",
  "name": "bndlift_reduce_invariant",
  "module_name": "TauLib.BookII.CentralTheorem.ExtensionsOmegaGerms",
  "module_url": "/verify/taulib/docs/book-ii-central-theorem-extensions-omega-germs/",
  "source_line_start": 308,
  "source_line_end": 311,
  "registry_ids": [
    "II.T38"
  ],
  "related_registry_items": [
    {
      "id": "II.T38",
      "title": "Extensions Are Omega-Germ Transformers",
      "url": "/registry/object/II.T38/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/ExtensionsOmegaGerms.lean#L308-L311",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/ExtensionsOmegaGerms.lean#L308-L311",
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
- Source path: [`TauLib/BookII/CentralTheorem/ExtensionsOmegaGerms.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/ExtensionsOmegaGerms.lean#L308-L311)
- Source range: L308-L311
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.T38` — Extensions Are Omega-Germ Transformers

## Immediate Comment / Docstring

```lean
/-- [II.T38] The bndlift extension at stage k depends only on reduce(x, k+1).
    bndlift(x, k) = bndlift(reduce(x, k+1), k).
    This is: reduce(x, k+1) = reduce(reduce(x, k+1), k+1),
    which is reduction idempotence. -/
```

## Source Excerpt

```lean
theorem bndlift_reduce_invariant (x k : TauIdx) :
    bndlift (reduce x (k + 1)) k = bndlift x k := by
  simp only [bndlift, reduce]
  exact Nat.mod_mod_of_dvd x (dvd_refl (primorial (k + 1)))
```
