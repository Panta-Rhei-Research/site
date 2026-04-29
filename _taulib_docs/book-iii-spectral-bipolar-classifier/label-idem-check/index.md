---
{
  "projection_kind": "taulib_declaration",
  "title": "label_idem_check",
  "permalink": "/verify/taulib/docs/book-iii-spectral-bipolar-classifier/label-idem-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectral.BipolarClassifier`.",
  "declaration_id": "TauLib.BookIII.Spectral.BipolarClassifier::label_idem_check",
  "declaration_slug": "label-idem-check",
  "kind": "def",
  "name": "label_idem_check",
  "module_name": "TauLib.BookIII.Spectral.BipolarClassifier",
  "module_url": "/verify/taulib/docs/book-iii-spectral-bipolar-classifier/",
  "source_line_start": 156,
  "source_line_end": 181,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/BipolarClassifier.lean#L156-L181",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/BipolarClassifier.lean#L156-L181",
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
- Source path: [`TauLib/BookIII/Spectral/BipolarClassifier.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/BipolarClassifier.lean#L156-L181)
- Source range: L156-L181
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.P08` — Label-Idempotent Compatibility

## Immediate Comment / Docstring

```lean
/-- [III.P08] Label-idempotent compatibility: B-type primes have
    e₊-dominant CRT basis, C-type have e₋-dominant.
    Verification via the bipolar decomposition of CRT basis elements. -/
```

## Source Excerpt

```lean
def label_idem_check (bound db : TauIdx) : Bool :=
  go 1 ((db + 1) * (bound + 1))
where
  go (i fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if i > bound then true
    else
      let p := nth_prime i
      if p > bound || p < 3 then go (i + 1) (fuel - 1)
      else
        let label := label_direct p
        -- Check CRT basis element projection at depth db
        if i > db then go (i + 1) (fuel - 1)
        else
          let basis := crt_basis db (i - 1)
          let bp := from_tau_idx basis
          let sp := interior_bipolar bp
          let b_dom := sp.b_sector.natAbs >= sp.c_sector.natAbs
          let c_dom := sp.c_sector.natAbs >= sp.b_sector.natAbs
          -- B-type should be b-dominant, C-type should be c-dominant
          let ok := match label with
            | .B => b_dom
            | .C => c_dom
            | .X => true  -- balanced, either is fine
          ok && go (i + 1) (fuel - 1)
  termination_by fuel
```
