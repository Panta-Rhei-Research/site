---
{
  "projection_kind": "taulib_declaration",
  "title": "teich_decomp_check_go",
  "permalink": "/verify/taulib/docs/book-i-polarity-teichmueller-lift/teich-decomp-check-go/",
  "summary_short": "`def` declaration in `TauLib.BookI.Polarity.TeichmuellerLift`.",
  "declaration_id": "TauLib.BookI.Polarity.TeichmuellerLift::teich_decomp_check_go",
  "declaration_slug": "teich-decomp-check-go",
  "kind": "def",
  "name": "teich_decomp_check_go",
  "module_name": "TauLib.BookI.Polarity.TeichmuellerLift",
  "module_url": "/verify/taulib/docs/book-i-polarity-teichmueller-lift/",
  "source_line_start": 100,
  "source_line_end": 108,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/TeichmuellerLift.lean#L100-L108",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.TeichmuellerLift",
        "url": "/verify/taulib/docs/book-i-polarity-teichmueller-lift/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/TeichmuellerLift.lean#L100-L108",
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

- Module: [TauLib.BookI.Polarity.TeichmuellerLift](/verify/taulib/docs/book-i-polarity-teichmueller-lift/)
- Source path: [`TauLib/BookI/Polarity/TeichmuellerLift.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/TeichmuellerLift.lean#L100-L108)
- Source range: L100-L108
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Decomposition check: nat_to_tail(n) = Σ teich_lift(n mod p_i, i, d). -/
```

## Source Excerpt

```lean
def teich_decomp_check_go (n d : TauIdx) (i fuel : Nat) (acc : List TauIdx) : List TauIdx :=
  if fuel = 0 then acc
  else if i ≥ d then acc
  else
    let lift_i := (teich_lift (n % nth_prime (i + 1)) i d).components
    let new_acc := (List.range d).map (fun j =>
      (acc.getD j 0 + lift_i.getD j 0) % primorial (j + 1))
    teich_decomp_check_go n d (i + 1) (fuel - 1) new_acc
termination_by fuel
```
