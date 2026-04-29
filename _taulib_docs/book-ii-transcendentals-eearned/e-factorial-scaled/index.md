---
{
  "projection_kind": "taulib_declaration",
  "title": "e_factorial_scaled",
  "permalink": "/verify/taulib/docs/book-ii-transcendentals-eearned/e-factorial-scaled/",
  "summary_short": "`def` declaration in `TauLib.BookII.Transcendentals.EEarned`.",
  "declaration_id": "TauLib.BookII.Transcendentals.EEarned::e_factorial_scaled",
  "declaration_slug": "e-factorial-scaled",
  "kind": "def",
  "name": "e_factorial_scaled",
  "module_name": "TauLib.BookII.Transcendentals.EEarned",
  "module_url": "/verify/taulib/docs/book-ii-transcendentals-eearned/",
  "source_line_start": 39,
  "source_line_end": 49,
  "registry_ids": [
    "II.D30"
  ],
  "related_registry_items": [
    {
      "id": "II.D30",
      "title": "e as Iterator Eigenvalue",
      "url": "/registry/object/II.D30/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/EEarned.lean#L39-L49",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/EEarned.lean#L39-L49",
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
- Source path: [`TauLib/BookII/Transcendentals/EEarned.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/EEarned.lean#L39-L49)
- Source range: L39-L49
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D30` — e as Iterator Eigenvalue

## Immediate Comment / Docstring

```lean
/-- [II.D30] e via factorial series: e = sum_{k=0}^{N} 1/k!
    Returns e * scale (approximately).
    Tracks the running factorial to avoid recomputation. -/
```

## Source Excerpt

```lean
def e_factorial_scaled (terms scale : Nat) : Nat :=
  go 0 (terms + 1) 1 0
where
  go (k fuel factorial acc : Nat) : Nat :=
    if fuel = 0 then acc
    else if k >= terms then acc
    else
      let fact := if k == 0 then 1 else factorial * k
      let term := scale / fact
      go (k + 1) (fuel - 1) fact (acc + term)
  termination_by fuel
```
