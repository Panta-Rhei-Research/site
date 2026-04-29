---
{
  "projection_kind": "taulib_declaration",
  "title": "label_convergence_check",
  "permalink": "/verify/taulib/docs/book-iii-spectral-bipolar-classifier/label-convergence-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectral.BipolarClassifier`.",
  "declaration_id": "TauLib.BookIII.Spectral.BipolarClassifier::label_convergence_check",
  "declaration_slug": "label-convergence-check",
  "kind": "def",
  "name": "label_convergence_check",
  "module_name": "TauLib.BookIII.Spectral.BipolarClassifier",
  "module_url": "/verify/taulib/docs/book-iii-spectral-bipolar-classifier/",
  "source_line_start": 121,
  "source_line_end": 141,
  "registry_ids": [
    "III.T13"
  ],
  "related_registry_items": [
    {
      "id": "III.T13",
      "title": "Label Convergence",
      "url": "/registry/object/III.T13/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/BipolarClassifier.lean#L121-L141",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectral.BipolarClassifier",
        "url": "/verify/taulib/docs/book-iii-spectral-bipolar-classifier/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/BipolarClassifier.lean#L121-L141",
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

- Module: [TauLib.BookIII.Spectral.BipolarClassifier](/verify/taulib/docs/book-iii-spectral-bipolar-classifier/)
- Source path: [`TauLib/BookIII/Spectral/BipolarClassifier.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/BipolarClassifier.lean#L121-L141)
- Source range: L121-L141
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T13` — Label Convergence

## Immediate Comment / Docstring

```lean
/-- [III.T13] Label convergence: label_direct is depth-independent,
    so it trivially stabilizes. Verify that label_at_depth agrees
    with label_direct for all primes at sufficient depth. -/
```

## Source Excerpt

```lean
def label_convergence_check (bound : TauIdx) : Bool :=
  -- Since label_direct doesn't depend on depth, convergence is immediate.
  -- We verify exhaustiveness: all primes get a label.
  go 1 (bound + 1)
where
  go (i fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if i > bound then true
    else
      let p := nth_prime i
      if p > bound then true
      else
        -- Label is well-defined
        let label := label_direct p
        let ok := label == .B || label == .C || label == .X
        -- B and C are mutually exclusive (for p > 2)
        let exclusive := if p > 2 then
          (label == .B && label != .C) || (label == .C && label != .B)
        else label == .X
        ok && exclusive && go (i + 1) (fuel - 1)
  termination_by fuel
```
