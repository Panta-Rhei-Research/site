---
{
  "projection_kind": "taulib_declaration",
  "title": "omega_germ_transformer_check",
  "permalink": "/verify/taulib/docs/book-ii-central-theorem-extensions-omega-germs/omega-germ-transformer-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.CentralTheorem.ExtensionsOmegaGerms`.",
  "declaration_id": "TauLib.BookII.CentralTheorem.ExtensionsOmegaGerms::omega_germ_transformer_check",
  "declaration_slug": "omega-germ-transformer-check",
  "kind": "def",
  "name": "omega_germ_transformer_check",
  "module_name": "TauLib.BookII.CentralTheorem.ExtensionsOmegaGerms",
  "module_url": "/verify/taulib/docs/book-ii-central-theorem-extensions-omega-germs/",
  "source_line_start": 144,
  "source_line_end": 160,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/ExtensionsOmegaGerms.lean#L144-L160",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/ExtensionsOmegaGerms.lean#L144-L160",
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
- Source path: [`TauLib/BookII/CentralTheorem/ExtensionsOmegaGerms.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/ExtensionsOmegaGerms.lean#L144-L160)
- Source range: L144-L160
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.T38` — Extensions Are Omega-Germ Transformers

## Immediate Comment / Docstring

```lean
/-- [II.T38] An omega-germ transformer from the bndlift extension:
    at each stage k, the extension defines a map
    f_k : Z/P_kZ -> Z/P_{k+1}Z given by f_k(x) = bndlift(x, k).

    Tower coherence of this family: reduce(f_{k+1}(x), k+1) = f_k(x).
    This is: reduce(bndlift(x, k+1), k+1) = bndlift(x, k)
    = reduce(x, k+1), which is reduction_compat (k+1 <= k+2). -/
```

## Source Excerpt

```lean
def omega_germ_transformer_check (bound db : TauIdx) : Bool :=
  go 2 1 ((bound + 1) * (db + 1))
where
  go (x k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k + 1 >= db then go (x + 1) 1 (fuel - 1)
    else
      -- The tower-coherent family: f_k(x) = bndlift(x, k)
      let f_k := bndlift x k
      let f_k1 := bndlift x (k + 1)
      -- Tower coherence: reduce(f_{k+1}(x), k+1) = f_k(x)
      let tower_ok := reduce f_k1 (k + 1) == f_k
      -- Stage-k coherence: reduce(f_k(x), k) = reduce(x, k)
      let stage_ok := reduce f_k k == reduce x k
      tower_ok && stage_ok && go x (k + 1) (fuel - 1)
  termination_by fuel
```
