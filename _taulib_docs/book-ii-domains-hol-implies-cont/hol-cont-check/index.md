---
{
  "projection_kind": "taulib_declaration",
  "title": "hol_cont_check",
  "permalink": "/verify/taulib/docs/book-ii-domains-hol-implies-cont/hol-cont-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Domains.HolImpliesCont`.",
  "declaration_id": "TauLib.BookII.Domains.HolImpliesCont::hol_cont_check",
  "declaration_slug": "hol-cont-check",
  "kind": "def",
  "name": "hol_cont_check",
  "module_name": "TauLib.BookII.Domains.HolImpliesCont",
  "module_url": "/verify/taulib/docs/book-ii-domains-hol-implies-cont/",
  "source_line_start": 105,
  "source_line_end": 116,
  "registry_ids": [
    "II.T06"
  ],
  "related_registry_items": [
    {
      "id": "II.T06",
      "title": "Holomorphic Implies Continuous",
      "url": "/registry/object/II.T06/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Domains/HolImpliesCont.lean#L105-L116",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Domains.HolImpliesCont",
        "url": "/verify/taulib/docs/book-ii-domains-hol-implies-cont/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Domains/HolImpliesCont.lean#L105-L116",
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

- Module: [TauLib.BookII.Domains.HolImpliesCont](/verify/taulib/docs/book-ii-domains-hol-implies-cont/)
- Source path: [`TauLib/BookII/Domains/HolImpliesCont.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Domains/HolImpliesCont.lean#L105-L116)
- Source range: L105-L116
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.T06` — Holomorphic Implies Continuous

## Immediate Comment / Docstring

```lean
/-- [II.T06] Hol ⟹ Cont: stage-local functions preserve
    agreement depth (1-Lipschitz in the ultrametric).
    If x,y agree at stage k, then f(x),f(y) agree at stage k.
    Flat double loop with single fuel counter. -/
```

## Source Excerpt

```lean
def hol_cont_check (sf : StageFun) (k_max bound : TauIdx) : Bool :=
  go 2 2 ((bound + 1) * (bound + 1))
where
  go (x y fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if y > bound then go (x + 1) 2 (fuel - 1)
    else
      let input_depth := disagree_depth x y k_max
      check_depth sf x y input_depth k_max &&
      go x (y + 1) (fuel - 1)
  termination_by fuel
```
