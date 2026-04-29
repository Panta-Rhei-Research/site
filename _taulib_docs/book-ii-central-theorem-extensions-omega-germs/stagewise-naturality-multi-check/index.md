---
{
  "projection_kind": "taulib_declaration",
  "title": "stagewise_naturality_multi_check",
  "permalink": "/verify/taulib/docs/book-ii-central-theorem-extensions-omega-germs/stagewise-naturality-multi-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.CentralTheorem.ExtensionsOmegaGerms`.",
  "declaration_id": "TauLib.BookII.CentralTheorem.ExtensionsOmegaGerms::stagewise_naturality_multi_check",
  "declaration_slug": "stagewise-naturality-multi-check",
  "kind": "def",
  "name": "stagewise_naturality_multi_check",
  "module_name": "TauLib.BookII.CentralTheorem.ExtensionsOmegaGerms",
  "module_url": "/verify/taulib/docs/book-ii-central-theorem-extensions-omega-germs/",
  "source_line_start": 118,
  "source_line_end": 131,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/ExtensionsOmegaGerms.lean#L118-L131",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/ExtensionsOmegaGerms.lean#L118-L131",
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
- Source path: [`TauLib/BookII/CentralTheorem/ExtensionsOmegaGerms.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/ExtensionsOmegaGerms.lean#L118-L131)
- Source range: L118-L131
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.L13` — Stagewise Naturality

## Immediate Comment / Docstring

```lean
/-- [II.L13] Multi-step naturality: reducing a bndlift extension
    across multiple stages is consistent.
    reduce(bndlift(x, k+m), k) = reduce(x, k) for any m >= 0. -/
```

## Source Excerpt

```lean
def stagewise_naturality_multi_check (bound db : TauIdx) : Bool :=
  go 2 1 1 ((bound + 1) * (db + 1) * (db + 1))
where
  go (x k m fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k >= db then go (x + 1) 1 1 (fuel - 1)
    else if k + m > db then go x (k + 1) 1 (fuel - 1)
    else
      let ext_km := bndlift x (k + m)
      let reduced := reduce ext_km k
      let direct := reduce x k
      (reduced == direct) && go x k (m + 1) (fuel - 1)
  termination_by fuel
```
