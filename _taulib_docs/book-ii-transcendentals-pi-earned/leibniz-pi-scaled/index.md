---
{
  "projection_kind": "taulib_declaration",
  "title": "leibniz_pi_scaled",
  "permalink": "/verify/taulib/docs/book-ii-transcendentals-pi-earned/leibniz-pi-scaled/",
  "summary_short": "`def` declaration in `TauLib.BookII.Transcendentals.PiEarned`.",
  "declaration_id": "TauLib.BookII.Transcendentals.PiEarned::leibniz_pi_scaled",
  "declaration_slug": "leibniz-pi-scaled",
  "kind": "def",
  "name": "leibniz_pi_scaled",
  "module_name": "TauLib.BookII.Transcendentals.PiEarned",
  "module_url": "/verify/taulib/docs/book-ii-transcendentals-pi-earned/",
  "source_line_start": 46,
  "source_line_end": 58,
  "registry_ids": [
    "II.D29"
  ],
  "related_registry_items": [
    {
      "id": "II.D29",
      "title": "Archimedes Polygon Sequence",
      "url": "/registry/object/II.D29/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/PiEarned.lean#L46-L58",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Transcendentals.PiEarned",
        "url": "/verify/taulib/docs/book-ii-transcendentals-pi-earned/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/PiEarned.lean#L46-L58",
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

- Module: [TauLib.BookII.Transcendentals.PiEarned](/verify/taulib/docs/book-ii-transcendentals-pi-earned/)
- Source path: [`TauLib/BookII/Transcendentals/PiEarned.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/PiEarned.lean#L46-L58)
- Source range: L46-L58
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D29` — Archimedes Polygon Sequence

## Immediate Comment / Docstring

```lean
/-- [II.D29] Leibniz series for pi: pi/4 = 1 - 1/3 + 1/5 - 1/7 + ...
    Returns pi * scale (approximately), computed as 4 * scale * sum.

    Uses separate positive and negative accumulators to avoid Nat underflow.
    Final result = 4 * (pos_sum - neg_sum) where each term = scale / (2k+1). -/
```

## Source Excerpt

```lean
def leibniz_pi_scaled (terms scale : Nat) : Nat :=
  let (pos, neg) := go 0 (terms + 1) 0 0
  if pos >= neg then pos - neg else 0
where
  go (k fuel pos neg : Nat) : Nat × Nat :=
    if fuel = 0 then (pos, neg)
    else if k >= terms then (pos, neg)
    else
      let denom := 2 * k + 1
      let term := 4 * scale / denom
      if k % 2 == 0 then go (k + 1) (fuel - 1) (pos + term) neg
      else go (k + 1) (fuel - 1) pos (neg + term)
  termination_by fuel
```
