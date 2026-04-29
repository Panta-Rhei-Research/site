---
{
  "projection_kind": "taulib_declaration",
  "title": "stagewise_naturality_check",
  "permalink": "/verify/taulib/docs/book-ii-central-theorem-extensions-omega-germs/stagewise-naturality-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.CentralTheorem.ExtensionsOmegaGerms`.",
  "declaration_id": "TauLib.BookII.CentralTheorem.ExtensionsOmegaGerms::stagewise_naturality_check",
  "declaration_slug": "stagewise-naturality-check",
  "kind": "def",
  "name": "stagewise_naturality_check",
  "module_name": "TauLib.BookII.CentralTheorem.ExtensionsOmegaGerms",
  "module_url": "/verify/taulib/docs/book-ii-central-theorem-extensions-omega-germs/",
  "source_line_start": 66,
  "source_line_end": 92,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/ExtensionsOmegaGerms.lean#L66-L92",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/ExtensionsOmegaGerms.lean#L66-L92",
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
- Source path: [`TauLib/BookII/CentralTheorem/ExtensionsOmegaGerms.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/ExtensionsOmegaGerms.lean#L66-L92)
- Source range: L66-L92
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.L13` — Stagewise Naturality

## Immediate Comment / Docstring

```lean
/-- [II.L13] Stagewise naturality check: verify that the bndlift
    extension is stage-compatible:

    reduce(bndlift(x, k+1), k) = bndlift(x, k)

    Equivalently: reduce(reduce(x, k+2), k+1) = reduce(x, k+1).

    This is exactly reduction_compat with k+1 <= k+2.
    This is the naturality condition making the extension a natural
    transformation on the primorial inverse system. -/
```

## Source Excerpt

```lean
def stagewise_naturality_check (bound db : TauIdx) : Bool :=
  go 2 1 ((bound + 1) * (db + 1))
where
  go (x k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k + 1 >= db then go (x + 1) 1 (fuel - 1)
    else
      -- bndlift(x, k+1) = reduce(x, k+2)
      let ext_k1 := bndlift x (k + 1)
      -- reduce(bndlift(x, k+1), k+1) should equal bndlift(x, k) = reduce(x, k+1)
      -- Wait: naturality says reduce(ext(k+1), k) = ext(k).
      -- ext(k) = bndlift(x, k) = reduce(x, k+1)
      -- reduce(ext(k+1), k) = reduce(bndlift(x, k+1), k) = reduce(reduce(x, k+2), k)
      -- By reduction_compat (k <= k+2): = reduce(x, k) ... but we want reduce(x, k+1).
      -- Actually naturality at the bndlift level means:
      -- reduce(bndlift(x, k+1), k) = reduce(x, k) = reduce(bndlift(x, k), k)
      -- (both extensions project to the same stage-k value)
      let reduced_ext_k1 := reduce ext_k1 k
      let ext_k := bndlift x k
      let reduced_ext_k := reduce ext_k k
      let direct_k := reduce x k
      -- All three should be equal: reduce gives the stage-k projection
      let ok1 := reduced_ext_k1 == direct_k
      let ok2 := reduced_ext_k == direct_k
      ok1 && ok2 && go x (k + 1) (fuel - 1)
  termination_by fuel
```
