---
{
  "projection_kind": "taulib_declaration",
  "title": "solenoidal_b_orbit",
  "permalink": "/verify/taulib/docs/book-ii-transcendentals-circles/solenoidal-b-orbit/",
  "summary_short": "`def` declaration in `TauLib.BookII.Transcendentals.Circles`.",
  "declaration_id": "TauLib.BookII.Transcendentals.Circles::solenoidal_b_orbit",
  "declaration_slug": "solenoidal-b-orbit",
  "kind": "def",
  "name": "solenoidal_b_orbit",
  "module_name": "TauLib.BookII.Transcendentals.Circles",
  "module_url": "/verify/taulib/docs/book-ii-transcendentals-circles/",
  "source_line_start": 38,
  "source_line_end": 39,
  "registry_ids": [
    "II.D26"
  ],
  "related_registry_items": [
    {
      "id": "II.D26",
      "title": "Solenoidal Circle",
      "url": "/registry/object/II.D26/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/Circles.lean#L38-L39",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Transcendentals.Circles",
        "url": "/verify/taulib/docs/book-ii-transcendentals-circles/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/Circles.lean#L38-L39",
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

- Module: [TauLib.BookII.Transcendentals.Circles](/verify/taulib/docs/book-ii-transcendentals-circles/)
- Source path: [`TauLib/BookII/Transcendentals/Circles.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/Circles.lean#L38-L39)
- Source range: L38-L39
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D26` — Solenoidal Circle

## Immediate Comment / Docstring

```lean
/-- [II.D26] Solenoidal B-orbit at the k-th prime: B mod p_k.
    This is the residue of the exponent coordinate in the k-th cyclic factor
    of the profinite group hat(Z). -/
```

## Source Excerpt

```lean
def solenoidal_b_orbit (x k : TauIdx) : TauIdx :=
  (from_tau_idx x).b % nth_prime k
```
