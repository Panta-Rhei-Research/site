---
{
  "projection_kind": "taulib_declaration",
  "title": "chi_p",
  "permalink": "/verify/taulib/docs/book-i-polarity-prime-polarity-classifier/chi-p/",
  "summary_short": "`def` declaration in `TauLib.BookI.Polarity.PrimePolarityClassifier`.",
  "declaration_id": "TauLib.BookI.Polarity.PrimePolarityClassifier::chi_p",
  "declaration_slug": "chi-p",
  "kind": "def",
  "name": "chi_p",
  "module_name": "TauLib.BookI.Polarity.PrimePolarityClassifier",
  "module_url": "/verify/taulib/docs/book-i-polarity-prime-polarity-classifier/",
  "source_line_start": 122,
  "source_line_end": 136,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/PrimePolarityClassifier.lean#L122-L136",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.PrimePolarityClassifier",
        "url": "/verify/taulib/docs/book-i-polarity-prime-polarity-classifier/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/PrimePolarityClassifier.lean#L122-L136",
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

- Module: [TauLib.BookI.Polarity.PrimePolarityClassifier](/verify/taulib/docs/book-i-polarity-prime-polarity-classifier/)
- Source path: [`TauLib/BookI/Polarity/PrimePolarityClassifier.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/PrimePolarityClassifier.lean#L122-L136)
- Source range: L122-L136
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Local quadratic character** at prime `p` (paper §6.5
    `chi-p-def`).

    For `p ≥ 3`: Legendre symbol via Euler's criterion
      `χ_p(a) := a^{(p-1)/2} mod p` (= 1 if QR, p-1 if QNR, 0 if p ∣ a).

    For `p = 2`: Kronecker convention
      `χ_2(a) := +1` if `a ≡ ±1 (mod 8)`,
                `-1` if `a ≡ ±3 (mod 8)`,
                `0` if `a` is even.

    For `p = 0` or `p = 1`: undefined → return 0 (sentinel).

    Returns `Int ∈ {-1, 0, +1}`. -/
```

## Source Excerpt

```lean
def chi_p (p a : Nat) : Int :=
  if p = 0 ∨ p = 1 then 0
  else if p = 2 then
    if a % 2 = 0 then 0
    else
      let r := a % 8
      if r = 1 ∨ r = 7 then 1 else -1
  else
    -- p ≥ 3: Euler's criterion via modPow
    if a % p = 0 then 0
    else
      let v := modPow (a % p) ((p - 1) / 2) p
      if v = 1 then 1
      else if v = p - 1 then -1
      else 0  -- shouldn't happen for prime p; sentinel
```
