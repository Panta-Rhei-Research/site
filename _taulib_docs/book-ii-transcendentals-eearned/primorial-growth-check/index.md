---
{
  "projection_kind": "taulib_declaration",
  "title": "primorial_growth_check",
  "permalink": "/verify/taulib/docs/book-ii-transcendentals-eearned/primorial-growth-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Transcendentals.EEarned`.",
  "declaration_id": "TauLib.BookII.Transcendentals.EEarned::primorial_growth_check",
  "declaration_slug": "primorial-growth-check",
  "kind": "def",
  "name": "primorial_growth_check",
  "module_name": "TauLib.BookII.Transcendentals.EEarned",
  "module_url": "/verify/taulib/docs/book-ii-transcendentals-eearned/",
  "source_line_start": 88,
  "source_line_end": 99,
  "registry_ids": [
    "II.D31"
  ],
  "related_registry_items": [
    {
      "id": "II.D31",
      "title": "Growth Base",
      "url": "/registry/object/II.D31/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/EEarned.lean#L88-L99",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Transcendentals.EEarned",
        "url": "/verify/taulib/docs/book-ii-transcendentals-eearned/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/EEarned.lean#L88-L99",
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

- Module: [TauLib.BookII.Transcendentals.EEarned](/verify/taulib/docs/book-ii-transcendentals-eearned/)
- Source path: [`TauLib/BookII/Transcendentals/EEarned.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/EEarned.lean#L88-L99)
- Source range: L88-L99
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D31` — Growth Base

## Immediate Comment / Docstring

```lean
/-- [II.D31] Growth base: consecutive primorial ratios.
    P_{k+1} / P_k = p_{k+1} >= 2 for all k >= 0.
    The primorial sequence grows super-exponentially. -/
```

## Source Excerpt

```lean
def primorial_growth_check (stages : TauIdx) : Bool :=
  go 1 (stages + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > stages then true
    else
      -- P_{k+1} / P_k = p_{k+1} >= 2
      let pk := primorial k
      let pk1 := primorial (k + 1)
      (pk > 0 && pk1 / pk >= 2) && go (k + 1) (fuel - 1)
  termination_by fuel
```
