---
{
  "projection_kind": "taulib_declaration",
  "title": "bsd_rank_agreement_check",
  "permalink": "/verify/taulib/docs/book-iii-arithmetic-bsd/bsd-rank-agreement-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Arithmetic.BSD`.",
  "declaration_id": "TauLib.BookIII.Arithmetic.BSD::bsd_rank_agreement_check",
  "declaration_slug": "bsd-rank-agreement-check",
  "kind": "def",
  "name": "bsd_rank_agreement_check",
  "module_name": "TauLib.BookIII.Arithmetic.BSD",
  "module_url": "/verify/taulib/docs/book-iii-arithmetic-bsd/",
  "source_line_start": 59,
  "source_line_end": 86,
  "registry_ids": [
    "III.T35"
  ],
  "related_registry_items": [
    {
      "id": "III.T35",
      "title": "BSD Coherence Theorem",
      "url": "/registry/object/III.T35/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/BSD.lean#L59-L86",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Arithmetic.BSD",
        "url": "/verify/taulib/docs/book-iii-arithmetic-bsd/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/BSD.lean#L59-L86",
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

- Module: [TauLib.BookIII.Arithmetic.BSD](/verify/taulib/docs/book-iii-arithmetic-bsd/)
- Source path: [`TauLib/BookIII/Arithmetic/BSD.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/BSD.lean#L59-L86)
- Source range: L59-L86
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T35` — BSD Coherence Theorem

## Immediate Comment / Docstring

```lean
/-- [III.T35] BSD functional-rank agreement: the BSD functional at level k
    is related to the number of stabilized rational points. -/
```

## Source Excerpt

```lean
def bsd_rank_agreement_check (db : TauIdx) : Bool :=
  go 0 1 (db + 1)
where
  go (dummy k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > db then true
    else
      let pk := primorial k
      if pk == 0 || pk > 100 then go 0 (k + 1) (fuel - 1)
      else
        -- All points are rational (rank well-defined)
        let all_rational := check_all_rational 0 pk k (pk + 1)
        -- Depth-sensitive: BSD functional captures tower structure
        let bsd_k := bsd_functional k
        let bp := split_zeta_b k
        let cp := split_zeta_c k
        -- Rank count × L-deriv decomposition is consistent with sector products
        let depth_ok := if k >= 2 && bp > 0 && cp > 0 then
          bsd_k > 0  -- non-trivial at sufficient depth
        else true
        all_rational && depth_ok && go 0 (k + 1) (fuel - 1)
  termination_by fuel
  check_all_rational (x pk k fuel2 : Nat) : Bool :=
    if fuel2 = 0 then true
    else if x >= pk then true
    else
      is_rational_at x k && check_all_rational (x + 1) pk k (fuel2 - 1)
  termination_by fuel2
```
