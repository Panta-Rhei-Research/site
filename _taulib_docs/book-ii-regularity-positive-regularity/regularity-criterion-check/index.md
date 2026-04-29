---
{
  "projection_kind": "taulib_declaration",
  "title": "regularity_criterion_check",
  "permalink": "/verify/taulib/docs/book-ii-regularity-positive-regularity/regularity-criterion-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Regularity.PositiveRegularity`.",
  "declaration_id": "TauLib.BookII.Regularity.PositiveRegularity::regularity_criterion_check",
  "declaration_slug": "regularity-criterion-check",
  "kind": "def",
  "name": "regularity_criterion_check",
  "module_name": "TauLib.BookII.Regularity.PositiveRegularity",
  "module_url": "/verify/taulib/docs/book-ii-regularity-positive-regularity/",
  "source_line_start": 179,
  "source_line_end": 192,
  "registry_ids": [
    "II.T34"
  ],
  "related_registry_items": [
    {
      "id": "II.T34",
      "title": "Regularity Criterion",
      "url": "/registry/object/II.T34/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/PositiveRegularity.lean#L179-L192",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Regularity.PositiveRegularity",
        "url": "/verify/taulib/docs/book-ii-regularity-positive-regularity/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/PositiveRegularity.lean#L179-L192",
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

- Module: [TauLib.BookII.Regularity.PositiveRegularity](/verify/taulib/docs/book-ii-regularity-positive-regularity/)
- Source path: [`TauLib/BookII/Regularity/PositiveRegularity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/PositiveRegularity.lean#L179-L192)
- Source range: L179-L192
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.T34` — Regularity Criterion

## Immediate Comment / Docstring

```lean
/-- [II.T34] Regularity criterion: x is regular iff both B-channel
    and C-channel are individually regular.

    is_regular(x, db) <=> is_b_regular(x, db) AND is_c_regular(x, db)

    This is the channel decomposition of regularity: the idempotent
    decomposition (II.L07) guarantees that stabilization decomposes
    into independent channel conditions. -/
```

## Source Excerpt

```lean
def regularity_criterion_check (bound db : TauIdx) : Bool :=
  go 2 (bound + 1)
where
  go (x fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else
      let reg := is_regular x db
      let b_reg := is_b_regular x db
      let c_reg := is_c_regular x db
      -- is_regular iff (is_b_regular AND is_c_regular)
      let ok := reg == (b_reg && c_reg)
      ok && go (x + 1) (fuel - 1)
  termination_by fuel
```
