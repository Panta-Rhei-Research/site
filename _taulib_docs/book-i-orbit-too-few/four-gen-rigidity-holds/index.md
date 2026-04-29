---
{
  "projection_kind": "taulib_declaration",
  "title": "four_gen_rigidity_holds",
  "permalink": "/verify/taulib/docs/book-i-orbit-too-few/four-gen-rigidity-holds/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Orbit.TooFew`.",
  "declaration_id": "TauLib.BookI.Orbit.TooFew::four_gen_rigidity_holds",
  "declaration_slug": "four-gen-rigidity-holds",
  "kind": "theorem",
  "name": "four_gen_rigidity_holds",
  "module_name": "TauLib.BookI.Orbit.TooFew",
  "module_url": "/verify/taulib/docs/book-i-orbit-too-few/",
  "source_line_start": 172,
  "source_line_end": 180,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/TooFew.lean#L172-L180",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Orbit.TooFew",
        "url": "/verify/taulib/docs/book-i-orbit-too-few/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/TooFew.lean#L172-L180",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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

- Module: [TauLib.BookI.Orbit.TooFew](/verify/taulib/docs/book-i-orbit-too-few/)
- Source path: [`TauLib/BookI/Orbit/TooFew.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/TooFew.lean#L172-L180)
- Source range: L172-L180
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Four-Generator Order-Preserving Rigidity**:
    Any order-preserving ρ-automorphism of the 4-generator system is the identity.

    Note: unlike the 5-generator system where rigidity holds for ALL automorphisms
    (given seed preservation at depth 0), the 4-generator system has rigidity only
    for ORDER-PRESERVING automorphisms. The transposition (π γ) is a valid
    non-order-preserving automorphism. This weaker form of rigidity is sufficient
    for the Minimal Alphabet Theorem. -/
```

## Source Excerpt

```lean
theorem four_gen_rigidity_holds :
    ∀ (f : Gen4 → Gen4),
      f alpha = alpha →
      f omega = omega →
      (∀ g h, Gen4.toNat g < Gen4.toNat h → Gen4.toNat (f g) < Gen4.toNat (f h)) →
      ∀ g, f g = g :=
  fun f ha ho hord => four_gen_order_rigid f ha ho hord

end Tau.Orbit.TooFew
```
