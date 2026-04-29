---
{
  "projection_kind": "taulib_declaration",
  "title": "code_spectral",
  "permalink": "/verify/taulib/docs/book-ii-regularity-code-decode/code-spectral/",
  "summary_short": "`def` declaration in `TauLib.BookII.Regularity.CodeDecode`.",
  "declaration_id": "TauLib.BookII.Regularity.CodeDecode::code_spectral",
  "declaration_slug": "code-spectral",
  "kind": "def",
  "name": "code_spectral",
  "module_name": "TauLib.BookII.Regularity.CodeDecode",
  "module_url": "/verify/taulib/docs/book-ii-regularity-code-decode/",
  "source_line_start": 73,
  "source_line_end": 74,
  "registry_ids": [
    "II.D51"
  ],
  "related_registry_items": [
    {
      "id": "II.D51",
      "title": "Code Map",
      "url": "/registry/object/II.D51/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/CodeDecode.lean#L73-L74",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Regularity.CodeDecode",
        "url": "/verify/taulib/docs/book-ii-regularity-code-decode/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/CodeDecode.lean#L73-L74",
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

- Module: [TauLib.BookII.Regularity.CodeDecode](/verify/taulib/docs/book-ii-regularity-code-decode/)
- Source path: [`TauLib/BookII/Regularity/CodeDecode.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/CodeDecode.lean#L73-L74)
- Source range: L73-L74
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D51` — Code Map

## Immediate Comment / Docstring

```lean
/-- [II.D51] Per-prime spectral coefficient: the projection of f onto
    the cylinder generator E_{k,pi,v}. This is proj_coeff from CanonicalBasis:
    code_spectral(f, k, pi, v) = sum_{x in Z/P_kZ : x%p == v} f(x)

    The spectral coefficients are the Fourier-like components of f
    decomposed along individual CRT factors. -/
```

## Source Excerpt

```lean
def code_spectral (f : TauIdx → Int) (k prime_idx v : TauIdx) : Int :=
  proj_coeff f k prime_idx v
```
