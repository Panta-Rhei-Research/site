---
{
  "projection_kind": "taulib_declaration",
  "title": "stagewise_naturality_strong_check",
  "permalink": "/verify/taulib/docs/book-ii-central-theorem-extensions-omega-germs/stagewise-naturality-strong-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.CentralTheorem.ExtensionsOmegaGerms`.",
  "declaration_id": "TauLib.BookII.CentralTheorem.ExtensionsOmegaGerms::stagewise_naturality_strong_check",
  "declaration_slug": "stagewise-naturality-strong-check",
  "kind": "def",
  "name": "stagewise_naturality_strong_check",
  "module_name": "TauLib.BookII.CentralTheorem.ExtensionsOmegaGerms",
  "module_url": "/verify/taulib/docs/book-ii-central-theorem-extensions-omega-germs/",
  "source_line_start": 98,
  "source_line_end": 113,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/ExtensionsOmegaGerms.lean#L98-L113",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/ExtensionsOmegaGerms.lean#L98-L113",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "status": "defined"
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
- Source path: [`TauLib/BookII/CentralTheorem/ExtensionsOmegaGerms.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/ExtensionsOmegaGerms.lean#L98-L113)
- Source range: L98-L113
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.L13` — Stagewise Naturality

## Immediate Comment / Docstring

```lean
/-- [II.L13] Stronger naturality: bndlift at successive stages
    is coherent: reduce(bndlift(x, k+1), k+1) = bndlift(x, k).
    This is: reduce(reduce(x, k+2), k+1) = reduce(x, k+1),
    which follows from reduction_compat since k+1 <= k+2. -/
```

## Source Excerpt

```lean
def stagewise_naturality_strong_check (bound db : TauIdx) : Bool :=
  go 2 1 ((bound + 1) * (db + 1))
where
  go (x k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k + 1 >= db then go (x + 1) 1 (fuel - 1)
    else
      -- reduce(bndlift(x, k+1), k+1) = reduce(reduce(x, k+2), k+1)
      let ext_k1 := bndlift x (k + 1)
      let reduced := reduce ext_k1 (k + 1)
      -- bndlift(x, k) = reduce(x, k+1)
      let ext_k := bndlift x k
      -- Should be equal
      (reduced == ext_k) && go x (k + 1) (fuel - 1)
  termination_by fuel
```
