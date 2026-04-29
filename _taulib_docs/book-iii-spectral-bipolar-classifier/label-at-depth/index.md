---
{
  "projection_kind": "taulib_declaration",
  "title": "label_at_depth",
  "permalink": "/verify/taulib/docs/book-iii-spectral-bipolar-classifier/label-at-depth/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectral.BipolarClassifier`.",
  "declaration_id": "TauLib.BookIII.Spectral.BipolarClassifier::label_at_depth",
  "declaration_slug": "label-at-depth",
  "kind": "def",
  "name": "label_at_depth",
  "module_name": "TauLib.BookIII.Spectral.BipolarClassifier",
  "module_url": "/verify/taulib/docs/book-iii-spectral-bipolar-classifier/",
  "source_line_start": 57,
  "source_line_end": 70,
  "registry_ids": [
    "III.D23"
  ],
  "related_registry_items": [
    {
      "id": "III.D23",
      "title": "Internal Bipolar Classifier",
      "url": "/registry/object/III.D23/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/BipolarClassifier.lean#L57-L70",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/BipolarClassifier.lean#L57-L70",
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
- Source path: [`TauLib/BookIII/Spectral/BipolarClassifier.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/BipolarClassifier.lean#L57-L70)
- Source range: L57-L70
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D23` — Internal Bipolar Classifier

## Immediate Comment / Docstring

```lean
/-- [III.D23] Classify a prime by its spectral behavior at depth n.
    Uses the CRT basis element e_i at depth n to determine the
    dominant channel of p_{i+1}:
    - B-type if CRT basis projects primarily to B-sector
    - C-type if CRT basis projects primarily to C-sector
    - X-type if balanced

    Concrete criterion: compare p mod 4.
    p ≡ 1 mod 4: B-type (quadratic residue structure, multiplicative)
    p ≡ 3 mod 4: C-type (non-residue structure, additive)
    p = 2: X-type (balanced, the crossing prime) -/
```

## Source Excerpt

```lean
def label_at_depth (p_idx n : TauIdx) : PrimeLabel :=
  let p := nth_prime p_idx
  if p < 2 then .X
  else if p == 2 then .X  -- 2 is the crossing prime
  else
    -- Use CRT projection at depth n to classify
    let basis := crt_basis n (p_idx - 1)  -- 0-indexed
    let bp := from_tau_idx basis
    let sp := interior_bipolar bp
    let b_val := sp.b_sector.natAbs
    let c_val := sp.c_sector.natAbs
    if b_val > c_val then .B
    else if c_val > b_val then .C
    else .X
```
