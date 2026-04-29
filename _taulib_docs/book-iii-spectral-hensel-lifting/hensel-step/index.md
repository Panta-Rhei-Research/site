---
{
  "projection_kind": "taulib_declaration",
  "title": "hensel_step",
  "permalink": "/verify/taulib/docs/book-iii-spectral-hensel-lifting/hensel-step/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectral.HenselLifting`.",
  "declaration_id": "TauLib.BookIII.Spectral.HenselLifting::hensel_step",
  "declaration_slug": "hensel-step",
  "kind": "def",
  "name": "hensel_step",
  "module_name": "TauLib.BookIII.Spectral.HenselLifting",
  "module_url": "/verify/taulib/docs/book-iii-spectral-hensel-lifting/",
  "source_line_start": 60,
  "source_line_end": 67,
  "registry_ids": [
    "III.T11"
  ],
  "related_registry_items": [
    {
      "id": "III.T11",
      "title": "Constructive Hensel Lifting",
      "url": "/registry/object/III.T11/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/HenselLifting.lean#L60-L67",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectral.HenselLifting",
        "url": "/verify/taulib/docs/book-iii-spectral-hensel-lifting/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/HenselLifting.lean#L60-L67",
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

- Module: [TauLib.BookIII.Spectral.HenselLifting](/verify/taulib/docs/book-iii-spectral-hensel-lifting/)
- Source path: [`TauLib/BookIII/Spectral/HenselLifting.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/HenselLifting.lean#L60-L67)
- Source range: L60-L67
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T11` — Constructive Hensel Lifting

## Immediate Comment / Docstring

```lean
/-- [III.T11] Hensel step: lift a root from mod p^k to mod p^(k+1).
    Newton correction: x_{k+1} = x_k - f(x_k) · f'(x_k)⁻¹ mod p^(k+1).
    Uses modular complement to avoid signed arithmetic:
    x - t ≡ x + (m - t) mod m. -/
```

## Source Excerpt

```lean
def hensel_step (a x _p _pk pk1 : TauIdx) : TauIdx :=
  if pk1 == 0 then x
  else
    let fx := poly_eval a x pk1
    let fpx := poly_deriv x pk1
    let inv_fpx := mod_inv fpx pk1
    let correction := (fx * inv_fpx) % pk1
    (x + pk1 - correction) % pk1
```
