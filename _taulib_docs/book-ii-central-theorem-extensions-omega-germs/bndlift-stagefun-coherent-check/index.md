---
{
  "projection_kind": "taulib_declaration",
  "title": "bndlift_stagefun_coherent_check",
  "permalink": "/verify/taulib/docs/book-ii-central-theorem-extensions-omega-germs/bndlift-stagefun-coherent-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.CentralTheorem.ExtensionsOmegaGerms`.",
  "declaration_id": "TauLib.BookII.CentralTheorem.ExtensionsOmegaGerms::bndlift_stagefun_coherent_check",
  "declaration_slug": "bndlift-stagefun-coherent-check",
  "kind": "def",
  "name": "bndlift_stagefun_coherent_check",
  "module_name": "TauLib.BookII.CentralTheorem.ExtensionsOmegaGerms",
  "module_url": "/verify/taulib/docs/book-ii-central-theorem-extensions-omega-germs/",
  "source_line_start": 176,
  "source_line_end": 194,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/ExtensionsOmegaGerms.lean#L176-L194",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/ExtensionsOmegaGerms.lean#L176-L194",
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
- Source path: [`TauLib/BookII/CentralTheorem/ExtensionsOmegaGerms.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/ExtensionsOmegaGerms.lean#L176-L194)
- Source range: L176-L194
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Tower coherence check for the bndlift StageFun:
    reduce(bndlift(x, l), k) = reduce(x, k) means the ABCD chart
    at stage k is determined by reduce(x, k), regardless of l >= k.
    So the B and C coordinates of from_tau_idx(reduce(bndlift(x,l), k))
    match those of from_tau_idx(reduce(x, k)). -/
```

## Source Excerpt

```lean
def bndlift_stagefun_coherent_check (bound db : TauIdx) : Bool :=
  go 2 1 ((bound + 1) * (db + 1))
where
  go (x k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k >= db then go (x + 1) 1 (fuel - 1)
    else
      -- B-coord of from_tau_idx(bndlift(x, k+1)) reduced to stage k
      let lifted_k1 := bndlift x (k + 1)
      let reduced_k := reduce lifted_k1 k
      let chart_reduced := from_tau_idx reduced_k
      -- B-coord of from_tau_idx(reduce(x, k))
      let chart_direct := from_tau_idx (reduce x k)
      -- Should match
      let b_ok := chart_reduced.b == chart_direct.b
      let c_ok := chart_reduced.c == chart_direct.c
      b_ok && c_ok && go x (k + 1) (fuel - 1)
  termination_by fuel
```
