---
{
  "projection_kind": "taulib_declaration",
  "title": "chi_extend",
  "permalink": "/verify/taulib/docs/book-i-polarity-polarity/chi-extend/",
  "summary_short": "`def` declaration in `TauLib.BookI.Polarity.Polarity`.",
  "declaration_id": "TauLib.BookI.Polarity.Polarity::chi_extend",
  "declaration_slug": "chi-extend",
  "kind": "def",
  "name": "chi_extend",
  "module_name": "TauLib.BookI.Polarity.Polarity",
  "module_url": "/verify/taulib/docs/book-i-polarity-polarity/",
  "source_line_start": 145,
  "source_line_end": 161,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/Polarity.lean#L145-L161",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.Polarity",
        "url": "/verify/taulib/docs/book-i-polarity-polarity/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/Polarity.lean#L145-L161",
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

- Module: [TauLib.BookI.Polarity.Polarity](/verify/taulib/docs/book-i-polarity-polarity/)
- Source path: [`TauLib/BookI/Polarity/Polarity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/Polarity.lean#L145-L161)
- Source range: L145-L161
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Multiplicative extension of Chi: sum Chi over prime factors with multiplicity.
    Chi_ext(n,N) = sum_{p^k || n} k * Chi(p,N). -/
```

## Source Excerpt

```lean
def chi_extend (n N : TauIdx) : Int :=
  if n ≤ 1 then 0
  else chi_go n N n
where
  chi_go (n N fuel : TauIdx) : Int :=
    if fuel = 0 then 0
    else if n ≤ 1 then 0
    else
      let p := largest_prime_divisor n
      if p ≤ 1 then 0
      else
        let v := p_adic_val p n
        let contrib := (v : Int) * polarity_chi p N
        let rest := n / (p ^ v)
        contrib + chi_go rest N (fuel - 1)
  termination_by fuel
  decreasing_by simp_wf; simp only [TauIdx] at *; omega
```
