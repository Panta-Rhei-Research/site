---
{
  "projection_kind": "taulib_declaration",
  "title": "split_complex_label_check",
  "permalink": "/verify/taulib/docs/book-iii-spectral-bipolar-classifier/split-complex-label-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectral.BipolarClassifier`.",
  "declaration_id": "TauLib.BookIII.Spectral.BipolarClassifier::split_complex_label_check",
  "declaration_slug": "split-complex-label-check",
  "kind": "def",
  "name": "split_complex_label_check",
  "module_name": "TauLib.BookIII.Spectral.BipolarClassifier",
  "module_url": "/verify/taulib/docs/book-iii-spectral-bipolar-classifier/",
  "source_line_start": 186,
  "source_line_end": 207,
  "registry_ids": [
    "III.P08"
  ],
  "related_registry_items": [
    {
      "id": "III.P08",
      "title": "Label-Idempotent Compatibility",
      "url": "/registry/object/III.P08/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/BipolarClassifier.lean#L186-L207",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/BipolarClassifier.lean#L186-L207",
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
- Source path: [`TauLib/BookIII/Spectral/BipolarClassifier.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/BipolarClassifier.lean#L186-L207)
- Source range: L186-L207
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.P08` — Label-Idempotent Compatibility

## Immediate Comment / Docstring

```lean
/-- [III.P08] Split-complex decomposition respects labels:
    B-type primes have CRT basis elements with b-dominant interior,
    C-type have c-dominant interior. -/
```

## Source Excerpt

```lean
def split_complex_label_check (bound db : TauIdx) : Bool :=
  go 1 (bound + 1)
where
  go (i fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if i > bound then true
    else
      let p := nth_prime i
      if p > bound || p < 3 || i > db then go (i + 1) (fuel - 1)
      else
        let basis := crt_basis db (i - 1)
        let bp := from_tau_idx basis
        let sp := interior_bipolar bp
        let label := label_direct p
        -- B-type: b_sector should be non-zero
        -- C-type: c_sector should be non-zero
        let ok := match label with
          | .B => sp.b_sector != 0
          | .C => sp.c_sector != 0
          | .X => true
        ok && go (i + 1) (fuel - 1)
  termination_by fuel
```
