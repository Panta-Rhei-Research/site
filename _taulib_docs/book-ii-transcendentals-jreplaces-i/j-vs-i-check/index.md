---
{
  "projection_kind": "taulib_declaration",
  "title": "j_vs_i_check",
  "permalink": "/verify/taulib/docs/book-ii-transcendentals-jreplaces-i/j-vs-i-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Transcendentals.JReplacesI`.",
  "declaration_id": "TauLib.BookII.Transcendentals.JReplacesI::j_vs_i_check",
  "declaration_slug": "j-vs-i-check",
  "kind": "def",
  "name": "j_vs_i_check",
  "module_name": "TauLib.BookII.Transcendentals.JReplacesI",
  "module_url": "/verify/taulib/docs/book-ii-transcendentals-jreplaces-i/",
  "source_line_start": 103,
  "source_line_end": 111,
  "registry_ids": [
    "II.T24"
  ],
  "related_registry_items": [
    {
      "id": "II.T24",
      "title": "j Replaces i",
      "url": "/registry/object/II.T24/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/JReplacesI.lean#L103-L111",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Transcendentals.JReplacesI",
        "url": "/verify/taulib/docs/book-ii-transcendentals-jreplaces-i/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/JReplacesI.lean#L103-L111",
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

- Module: [TauLib.BookII.Transcendentals.JReplacesI](/verify/taulib/docs/book-ii-transcendentals-jreplaces-i/)
- Source path: [`TauLib/BookII/Transcendentals/JReplacesI.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/JReplacesI.lean#L103-L111)
- Source range: L103-L111
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.T24` — j Replaces i

## Immediate Comment / Docstring

```lean
/-- [II.T24] j replaces i: comprehensive comparison.

    1. j^2 = +1 (split-complex, hyperbolic)
    2. i^2 = -1 (Gaussian, elliptic)
    3. j admits nontrivial idempotents; i does not (I.T10)
    4. Zero divisors in H_tau witness polarity structure

    The wave equation u_tt = u_xx comes from j^2 = +1.
    The Laplace equation u_tt + u_xx = 0 would come from i^2 = -1.
    Category tau chooses j (waves, polarity) over i (rotation). -/
```

## Source Excerpt

```lean
def j_vs_i_check : Bool :=
  -- j^2 = +1 (split-complex)
  SplitComplex.mul ⟨0, 1⟩ ⟨0, 1⟩ == ⟨1, 0⟩ &&
  -- i^2 = -1 (Gaussian): (0,1)*(0,1) = (0*0 - 1*1, 0*1 + 1*0) = (-1, 0)
  GaussInt.mul ⟨0, 1⟩ ⟨0, 1⟩ == ⟨-1, 0⟩ &&
  -- j has nontrivial idempotents
  idempotent_check &&
  -- Zero divisors exist: (1+j)(1-j) = 0
  SplitComplex.mul ⟨1, 1⟩ ⟨1, -1⟩ == SplitComplex.zero
```
