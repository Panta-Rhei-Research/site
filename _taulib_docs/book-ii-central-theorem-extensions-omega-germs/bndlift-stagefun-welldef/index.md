---
{
  "projection_kind": "taulib_declaration",
  "title": "bndlift_stagefun_welldef",
  "permalink": "/verify/taulib/docs/book-ii-central-theorem-extensions-omega-germs/bndlift-stagefun-welldef/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.CentralTheorem.ExtensionsOmegaGerms`.",
  "declaration_id": "TauLib.BookII.CentralTheorem.ExtensionsOmegaGerms::bndlift_stagefun_welldef",
  "declaration_slug": "bndlift-stagefun-welldef",
  "kind": "theorem",
  "name": "bndlift_stagefun_welldef",
  "module_name": "TauLib.BookII.CentralTheorem.ExtensionsOmegaGerms",
  "module_url": "/verify/taulib/docs/book-ii-central-theorem-extensions-omega-germs/",
  "source_line_start": 318,
  "source_line_end": 320,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/ExtensionsOmegaGerms.lean#L318-L320",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/ExtensionsOmegaGerms.lean#L318-L320",
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
- Source path: [`TauLib/BookII/CentralTheorem/ExtensionsOmegaGerms.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/ExtensionsOmegaGerms.lean#L318-L320)
- Source range: L318-L320
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.T38` — Extensions Are Omega-Germ Transformers

## Immediate Comment / Docstring

```lean
/-- [II.T38] Tower coherence of bndlift StageFun inputs:
    the ABCD chart at stage k is determined by reduce(x, k).
    For the bndlift StageFun, from_tau_idx(bndlift(x, k)) =
    from_tau_idx(bndlift(reduce(x, k+1), k)) =
    from_tau_idx(bndlift(x, k)) by bndlift_reduce_invariant. -/
```

## Source Excerpt

```lean
theorem bndlift_stagefun_welldef (x k : TauIdx) :
    bndlift (reduce x (k + 1)) k = bndlift x k :=
  bndlift_reduce_invariant x k
```
