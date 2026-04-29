---
{
  "projection_kind": "taulib_declaration",
  "title": "TowerCoherent",
  "permalink": "/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/tower-coherent/",
  "summary_short": "`def` declaration in `TauLib.BookI.Holomorphy.TauHolomorphic`.",
  "declaration_id": "TauLib.BookI.Holomorphy.TauHolomorphic::TowerCoherent",
  "declaration_slug": "tower-coherent",
  "kind": "def",
  "name": "TowerCoherent",
  "module_name": "TauLib.BookI.Holomorphy.TauHolomorphic",
  "module_url": "/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/",
  "source_line_start": 71,
  "source_line_end": 73,
  "registry_ids": [
    "I.D46"
  ],
  "related_registry_items": [
    {
      "id": "I.D46",
      "title": "Tower Coherence",
      "url": "/registry/object/I.D46/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/TauHolomorphic.lean#L71-L73",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Holomorphy.TauHolomorphic",
        "url": "/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/TauHolomorphic.lean#L71-L73",
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

- Module: [TauLib.BookI.Holomorphy.TauHolomorphic](/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/)
- Source path: [`TauLib/BookI/Holomorphy/TauHolomorphic.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/TauHolomorphic.lean#L71-L73)
- Source range: L71-L73
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `I.D46` — Tower Coherence

## Immediate Comment / Docstring

```lean
/-- [I.D46] Tower coherence for a stagewise sector function:
    reducing the output from stage ℓ to stage k agrees with
    computing the output at stage k directly.

    For the B-sector: reduce(f.b_fun(n, ℓ), k) = f.b_fun(n, k)
    For the C-sector: reduce(f.c_fun(n, ℓ), k) = f.c_fun(n, k)

    This is a NATURALITY condition on the primorial inverse system. -/
```

## Source Excerpt

```lean
def TowerCoherent (f : StageFun) : Prop :=
  (∀ n k l : TauIdx, k ≤ l → reduce (f.b_fun n l) k = f.b_fun n k) ∧
  (∀ n k l : TauIdx, k ≤ l → reduce (f.c_fun n l) k = f.c_fun n k)
```
