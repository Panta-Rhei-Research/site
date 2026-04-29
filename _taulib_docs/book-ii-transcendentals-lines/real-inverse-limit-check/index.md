---
{
  "projection_kind": "taulib_declaration",
  "title": "real_inverse_limit_check",
  "permalink": "/verify/taulib/docs/book-ii-transcendentals-lines/real-inverse-limit-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Transcendentals.Lines`.",
  "declaration_id": "TauLib.BookII.Transcendentals.Lines::real_inverse_limit_check",
  "declaration_slug": "real-inverse-limit-check",
  "kind": "def",
  "name": "real_inverse_limit_check",
  "module_name": "TauLib.BookII.Transcendentals.Lines",
  "module_url": "/verify/taulib/docs/book-ii-transcendentals-lines/",
  "source_line_start": 92,
  "source_line_end": 102,
  "registry_ids": [
    "II.T20"
  ],
  "related_registry_items": [
    {
      "id": "II.T20",
      "title": "R as Inverse Limit",
      "url": "/registry/object/II.T20/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/Lines.lean#L92-L102",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Transcendentals.Lines",
        "url": "/verify/taulib/docs/book-ii-transcendentals-lines/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/Lines.lean#L92-L102",
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

- Module: [TauLib.BookII.Transcendentals.Lines](/verify/taulib/docs/book-ii-transcendentals-lines/)
- Source path: [`TauLib/BookII/Transcendentals/Lines.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/Lines.lean#L92-L102)
- Source range: L92-L102
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.T20` — R as Inverse Limit

## Immediate Comment / Docstring

```lean
/-- [II.T20] R as inverse limit: at each stage k, the number of distinct
    D-residues is positive and bounded by primorial(k).
    The D-residue space grows with the primorial, witnessing the inverse
    limit structure lim Z/P_k Z = Z_hat -> R. -/
```

## Source Excerpt

```lean
def real_inverse_limit_check (a bound stages : TauIdx) : Bool :=
  go 1 (stages + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > stages then true
    else
      let d_res := count_d_residues a k bound
      -- D-residue count is positive and bounded by primorial(k)
      d_res > 0 && d_res <= primorial k && go (k + 1) (fuel - 1)
  termination_by fuel
```
