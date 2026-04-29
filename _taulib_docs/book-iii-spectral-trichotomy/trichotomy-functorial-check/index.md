---
{
  "projection_kind": "taulib_declaration",
  "title": "trichotomy_functorial_check",
  "permalink": "/verify/taulib/docs/book-iii-spectral-trichotomy/trichotomy-functorial-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectral.Trichotomy`.",
  "declaration_id": "TauLib.BookIII.Spectral.Trichotomy::trichotomy_functorial_check",
  "declaration_slug": "trichotomy-functorial-check",
  "kind": "def",
  "name": "trichotomy_functorial_check",
  "module_name": "TauLib.BookIII.Spectral.Trichotomy",
  "module_url": "/verify/taulib/docs/book-iii-spectral-trichotomy/",
  "source_line_start": 94,
  "source_line_end": 115,
  "registry_ids": [
    "III.T14"
  ],
  "related_registry_items": [
    {
      "id": "III.T14",
      "title": "Spectral Trichotomy Lemma",
      "url": "/registry/object/III.T14/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/Trichotomy.lean#L94-L115",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectral.Trichotomy",
        "url": "/verify/taulib/docs/book-iii-spectral-trichotomy/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/Trichotomy.lean#L94-L115",
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

- Module: [TauLib.BookIII.Spectral.Trichotomy](/verify/taulib/docs/book-iii-spectral-trichotomy/)
- Source path: [`TauLib/BookIII/Spectral/Trichotomy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/Trichotomy.lean#L94-L115)
- Source range: L94-L115
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T14` — Spectral Trichotomy Lemma

## Immediate Comment / Docstring

```lean
/-- [III.T14] Trichotomy functoriality: the decomposition commutes
    with level change (reduction from k+1 to k). -/
```

## Source Excerpt

```lean
def trichotomy_functorial_check (bound db : TauIdx) : Bool :=
  go 0 1 ((bound + 1) * (db + 1))
where
  go (x k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k >= db then go (x + 1) 1 (fuel - 1)
    else
      -- Decompose at k+1, then reduce to k
      let res_high := crt_decompose x (k + 1)
      let (b_high, _c_high, _x_high) := trichotomy_decompose res_high (k + 1)
      -- Decompose at k directly
      let res_low := crt_decompose x k
      let (b_low, _c_low, _x_low) := trichotomy_decompose res_low k
      -- B-part at k should match first k components of B-part at k+1
      let consistent := check_prefix b_high b_low 0 k
      consistent && go x (k + 1) (fuel - 1)
  termination_by fuel
  check_prefix (high low : List TauIdx) (i k : Nat) : Bool :=
    if i >= k then true
    else
      high.getD i 0 == low.getD i 0 && check_prefix high low (i + 1) k
```
