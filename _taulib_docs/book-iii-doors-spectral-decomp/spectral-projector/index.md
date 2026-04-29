---
{
  "projection_kind": "taulib_declaration",
  "title": "spectral_projector",
  "permalink": "/verify/taulib/docs/book-iii-doors-spectral-decomp/spectral-projector/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Doors.SpectralDecomp`.",
  "declaration_id": "TauLib.BookIII.Doors.SpectralDecomp::spectral_projector",
  "declaration_slug": "spectral-projector",
  "kind": "def",
  "name": "spectral_projector",
  "module_name": "TauLib.BookIII.Doors.SpectralDecomp",
  "module_url": "/verify/taulib/docs/book-iii-doors-spectral-decomp/",
  "source_line_start": 54,
  "source_line_end": 60,
  "registry_ids": [
    "III.D80"
  ],
  "related_registry_items": [
    {
      "id": "III.D80",
      "title": "q-Expansion Coefficients",
      "url": "/registry/object/III.D80/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SpectralDecomp.lean#L54-L60",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Doors.SpectralDecomp",
        "url": "/verify/taulib/docs/book-iii-doors-spectral-decomp/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SpectralDecomp.lean#L54-L60",
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

- Module: [TauLib.BookIII.Doors.SpectralDecomp](/verify/taulib/docs/book-iii-doors-spectral-decomp/)
- Source path: [`TauLib/BookIII/Doors/SpectralDecomp.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SpectralDecomp.lean#L54-L60)
- Source range: L54-L60
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D80` — q-Expansion Coefficients

## Immediate Comment / Docstring

```lean
/-- [III.D80] Spectral projector: P_n(f) = ⟨f, e_n⟩ · e_n.
    For the discrete model with N points, e_n(x) = exp(2πinx/N).
    We use the real part: cos(2πnx/N), approximated by the indicator
    of the n-th frequency bin.

    Simplified: at stage k with M_k points, the n-th mode projector
    extracts the n-th Fourier coefficient. For computational verification,
    we use the orthogonal basis of indicator functions. -/
```

## Source Excerpt

```lean
def spectral_projector (n : Nat) (f : Nat → Int) (N : Nat) (x : Nat) : Int :=
  if N == 0 then 0
  else
    -- Coefficient: c_n = Σ_{y} f(y) · δ_{y,n}  (indicator basis)
    let coeff := if n < N then f n else 0
    -- P_n(f)(x) = c_n · δ_{x,n}
    if x == n then coeff else 0
```
