---
{
  "projection_kind": "taulib_declaration",
  "title": "integral_linearity_check",
  "permalink": "/verify/taulib/docs/book-i-boundary-integration/integral-linearity-check/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.Integration`.",
  "declaration_id": "TauLib.BookI.Boundary.Integration::integral_linearity_check",
  "declaration_slug": "integral-linearity-check",
  "kind": "def",
  "name": "integral_linearity_check",
  "module_name": "TauLib.BookI.Boundary.Integration",
  "module_url": "/verify/taulib/docs/book-i-boundary-integration/",
  "source_line_start": 69,
  "source_line_end": 77,
  "registry_ids": [
    "I.T51"
  ],
  "related_registry_items": [
    {
      "id": "I.T51",
      "title": "Linearity of Integration",
      "url": "/registry/object/I.T51/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Integration.lean#L69-L77",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.Integration",
        "url": "/verify/taulib/docs/book-i-boundary-integration/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Integration.lean#L69-L77",
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

- Module: [TauLib.BookI.Boundary.Integration](/verify/taulib/docs/book-i-boundary-integration/)
- Source path: [`TauLib/BookI/Boundary/Integration.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Integration.lean#L69-L77)
- Source range: L69-L77
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `I.T51` — Linearity of Integration

## Immediate Comment / Docstring

```lean
/-- [I.T51] Check linearity: ∫(af + bg) = a∫f + b∫g at stage k. -/
```

## Source Excerpt

```lean
def integral_linearity_check (a b : Int) (f g : Nat → Int) (k : Nat) : Bool :=
  let intf := tau_integral f k
  let intg := tau_integral g k
  let intfg := tau_integral (fun x => a * f x + b * g x) k
  let pk := primorial k
  -- ∫(af + bg) = a∫f + b∫g as rationals:
  -- intfg.num / pk = a * intf.num / pk + b * intg.num / pk
  -- i.e., intfg.num = a * intf.num + b * intg.num
  intfg.numerator == a * intf.numerator + b * intg.numerator
```
